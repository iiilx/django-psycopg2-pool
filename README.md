# django-psycopg2-pool
--------------------

## Features
-----------

* Basic postgres connection pool for Django using gevent
** assumes you monkeypatch somewhere when using this backend

## Installing the app
----------------------
    clone via git and python setup.py install
   
OR

    easy_install django-psycopg2-pool

## Setting up the app
----------------------

Assuming you have Django installed and this app installed,

1. set `ENGINE` to `'django_psycopg2_pool.gevent'` in your db backend settings
2. this may be required if you have south: in settings.py, have a line like:

<!-- language: python -->
    SOUTH_DATABASE_ADAPTERS = {
        'default': "south.db.postgresql_psycopg2",
    }

3. Set `POOL_SIZE` to 100 or so in your db settings and tweak this number so that each worker process has adequate postgres connections available to it.  If you have four worker processes and `max_connections` for postgres is 101, then 25 is a reasonable pool size that will still let you run manage commands like south.  Each connection to postgres will fork a postgres worker, visible running `pstree -pa` on Linux systems.  Raising `max_connections` in postgres can consume a lot of memory if `work_mem` is set high.  Work_mem is necessary to do in-memory sorts before spilling to the disk, so don't set this too low just to have tons of postgres threads running.

<!-- language: python -->
    DATABASES = {
        'default': {
            'ENGINE': 'django_psycopg2_pool.gevent', 
            'NAME': 'myproject_db',                  
            'USER': 'myproject',                    
            'PASSWORD': 'mypassword',                
            'HOST': '/var/run/postgresql',           # When running postgres on unix socket
            'PORT': '',                              # Empty if using unix socket
            'POOL_SIZE' : 20,                        # slightly less than postgres max_connections / worker processes
        }
    }

## NOTES
---------
This package includes a modified version of the gevent example psycopg2_pool
Thank you to the author(s) of gevent and psyocopg2_pool

# CONTRIBUTE
-----------
* feel free to contribute!
* maybe this can be done in eventlet as well? I welcome pull requests


