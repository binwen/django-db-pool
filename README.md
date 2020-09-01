通过DBUtils库实现Django数据库连接池，目前支持mysql、postgresql 数据库.

下面的配置参考：
-----------
```python
DATABASES = {
   'default':{
        'ENGINE': 'djdbpool.db.backends.mysql',
        "HOST": "127.0.0.1",
        "NAME": "test_db",
        "PASSWORD": "",
        "USER": "django",
        "PORT": 3306,
        'OPTIONS': {'charset': 'utf8mb4'},
        'POOL': {  # 更多的配置请参考DBUtils的配置
           'minsize': 5, # 初始化时，连接池中至少创建的空闲的链接，0表示不创建，不填默认为5
           'maxsize': 10,  # 连接池中最多闲置的链接，0不限制，不填默认为0
           'maxconnections': 60, # 连接池允许的最大连接数，0表示不限制连接数, 默认为0
           'blocking': True, # 连接池中如果没有可用连接后，是否阻塞等待。True:等待；False:不等待然后报错, 默认False
           'ping':0  # 检查服务是否可用 1检查0不检查
        }
    }
}

```
