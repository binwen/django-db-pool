# -*- coding: utf-8 -*-
import six
from django.core.exceptions import ImproperlyConfigured
from django.db.backends.mysql.base import DatabaseWrapper as MysqlDatabaseWrapper
from django.utils.safestring import  SafeText,SafeData

class SafeBytes(bytes, SafeData):
    """
	A bytes subclass that has been specifically marked as "safe" (requires no
	further escaping) for HTML output purposes.

	Kept in Django 2.0 for usage by apps supporting Python 2. Shouldn't be used
	in Django anymore.
	"""
    
    def __add__(self, rhs):
        """
		Concatenating a safe byte string with another safe byte string or safe
		string is safe. Otherwise, the result is no longer safe.
		"""
        t = super().__add__(rhs)
        if isinstance(rhs, SafeText):
            return SafeText(t)
        elif isinstance(rhs, SafeBytes):
            return SafeBytes(t)
        return t


try:
    import MySQLdb as Database
except ImportError as err:
    try:
        import pymysql as Database
    except ImportError:
        raise ImproperlyConfigured("Error loading MySQLdb or pymsql module.\n Did you install mysqlclient or pymysql")

from djdbpool.db.pool import DBPoolWrapper


Database = DBPoolWrapper(Database)


class DatabaseWrapper(MysqlDatabaseWrapper):

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
        conn = Database.connect(**conn_params)
        conn.encoders[SafeText] = conn.encoders[six.text_type]
        conn.encoders[SafeBytes] = conn.encoders[bytes]
        return conn
