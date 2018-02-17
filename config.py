#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2017/11/28 下午4:57
# @Author : Matrix
# @Github : https://github.com/blackmatrix7/
# @Blog : http://www.cnblogs.com/blackmatrix/
# @File : config.py
# @Software: PyCharm
from toolkit.config import BaseConfig, get_current_config

__author__ = 'blackmatrix'


class CommonConfig(BaseConfig):

    DATE_FMT = '%Y-%m-%d'
    DATETIME_FMT = '%Y-%m-%d %H:%M:%S'

    # Cache
    CACHE_MEMCACHED_SERVERS = ['127.0.0.1:11211']
    CACHE_REDIS_SERVERS = '127.0.0.1'
    CACHE_REDIS_PORT = '6379'
    CACHE_REDIS_DB = 0

    # DingTalk
    DING_DOMAIN = 'testdomain'
    DING_CORP_ID = None
    DING_CORP_SECRET = None
    DING_AGENT_ID = None
    DING_AES_KEY = None
    # 钉钉回调地址，必须返回含有success字符串的json格式
    DING_CALLBACK = None

    # 钉钉会话存储
    DING_SESSION_HOST = '127.0.0.1'
    DING_SESSION_PORT = 3306
    DING_SESSION_USER = 'root'
    DING_SESSION_PASS = 'password'
    DING_SESSION_DB = 'DingTalkCache'

    @property
    def ding_session_manager(self):
        # memcached
        from memcache import Client
        cache = Client(self.CACHE_MEMCACHED_SERVERS)
        return cache

    DING_SESSION_MANAGER = ding_session_manager


class DevConfig(CommonConfig):

    # Cache
    CACHE_MEMCACHED_SERVERS = ['127.0.0.1:11211']


default = CommonConfig()
devcfg = DevConfig()

configs = {'default': default,
           'devcfg': devcfg}

# 读取配置文件的名称，在具体的应用中，可以从环境变量、命令行参数等位置获取配置文件名称
config_name = 'default'

current_config = get_current_config(config_name)
