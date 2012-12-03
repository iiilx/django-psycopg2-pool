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

1. add 'django-psycopg2-pool.gevent' as your db backend
2. this may be required if you have south: in settings.py, have a line like:

    SOUTH_DATABASE_ADAPTERS = {
        'default': "south.db.postgresql_psycopg2",
    }

3. add ''POOL_SIZE' : 100,' to your db backend options and tweak this number so that each worker process has adequate postgres connections available to it.  Each connection to postgres will fork a postgres worker, visible running 'pstree -pa' on Linux systems.  Raising max_connections in postgres can consume a lot of memory if work_mem is set high.  Work_mem is necessary to do in-memory sorts before spilling to the disk, so don't set this too low just to have tons of postgres threads running.


## NOTES
---------
This package includes a modified version of the gevent example psycopg2_pool
Thank you to the author(s) of gevent and psyocopg2_pool

# CONTRIBUTE
-----------
* feel free to contribute!
* maybe this can be done in eventlet as well? I welcome pull requests


