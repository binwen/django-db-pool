# -*- coding: utf-8 -*-
try:
    from DBUtils.PooledDB import PooledDB
    from DBUtils.SteadyDB import SteadyDBConnection
except ImportError:
    from dbutils.pooled_db import PooledDB
    from dbutils.steady_db import SteadyDBConnection


class DBPoolWrapper(object):
    def __init__(self, db_module):
        self._connection = None
        self._db_module = db_module
        self._pool = {}

    def __getattr__(self, item):
        return getattr(self._db_module, item)

    def connect(self, **kwargs):
        db = kwargs.get("db", "")
        if db not in self._pool:
            self._pool[db] = PooledDB(creator=self._db_module, **kwargs)
        self._connection = self._pool[db].connection()
        return self._connection


def autocommit(self, *args, **kwargs):
    self._con.autocommit(*args, **kwargs)


def get_server_info(self):
    return self._con.get_server_info()


@property
def encoders(self):
    return self._con.encoders


#  postgresql
@property
def isolation_level(self):
    return self._con.isolation_level


def set_client_encoding(self, encoding):
    return self._con.set_client_encoding(encoding)


def get_parameter_status(self, parameter):
    return self._con.get_parameter_status(parameter)


setattr(SteadyDBConnection, "autocommit", autocommit)
setattr(SteadyDBConnection, "get_server_info", get_server_info)
setattr(SteadyDBConnection, "encoders", encoders)
setattr(SteadyDBConnection, "isolation_level", isolation_level)
setattr(SteadyDBConnection, "set_client_encoding", set_client_encoding)
setattr(SteadyDBConnection, "get_parameter_status", get_parameter_status)
