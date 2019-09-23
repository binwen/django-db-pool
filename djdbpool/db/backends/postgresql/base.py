# -*- coding: utf-8 -*-
from django.core.exceptions import ImproperlyConfigured

try:
    import psycopg2 as Database
    import psycopg2.extensions
    import psycopg2.extras
except ImportError as e:
    raise ImproperlyConfigured("Error loading psycopg2 module: %s" % e)

from django.db.backends.postgresql.base import DatabaseWrapper as PostgresDatabaseWrapper
from djdbpool.db.pool import DBPoolWrapper


Database = DBPoolWrapper(Database)


class DatabaseWrapper(PostgresDatabaseWrapper):
    Database = Database

    def get_connection_params(self):
        params = super(DatabaseWrapper, self).get_connection_params()
        pool_config = self.settings_dict.get('POOL', {})
        minsize = pool_config.pop("minsize", 5)
        maxsize = pool_config.pop("maxsize", 0)
        params["mincached"] = int(minsize)
        params["maxcached"] = int(maxsize)
        params.update(pool_config)

        return params

    def get_new_connection(self, conn_params):
        connection = Database.connect(**conn_params)
        options = self.settings_dict['OPTIONS']
        try:
            self.isolation_level = options['isolation_level']
        except KeyError:
            self.isolation_level = connection.isolation_level
        else:
            # Set the isolation level to the value from OPTIONS.
            if self.isolation_level != connection.isolation_level:
                connection.set_session(isolation_level=self.isolation_level)
        return connection
