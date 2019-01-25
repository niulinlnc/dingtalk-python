#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2017/11/30 下午2:50
# @Author : Matrix
# @Github : https://github.com/blackmatrix7/
# @Blog : http://www.cnblogs.com/blackmatrix/
# @File : customers.py
# @Software: PyCharm
import json
from ..foundation import call_dingtalk_webapi, dingtalk_resp, call_topapi

__author__ = 'blackmatrix'

__all__ = ['get_corp_ext_list', 'add_corp_ext', 'update_corp_ext', 'delete_corp_ext']


@dingtalk_resp
def get_corp_ext_list(access_token, size=20, offset=0):
    """
    获取外部联系人
    :return:
    """
    return call_dingtalk_webapi(access_token, 'dingtalk.corp.ext.list', 'GET', size=size, offset=offset)


@dingtalk_resp
def add_corp_ext(access_token, contact: dict):
    """
    新增外部联系人
    :return:
    """
    contact = json.dumps(contact)
    data = call_dingtalk_webapi(access_token, 'dingtalk.corp.ext.add', 'POST', contact=contact)
    return data


@dingtalk_resp
def update_corp_ext(access_token, contact: dict):
    """
    更新外部联系人
    :return:
    """
    contact = json.dumps(contact)
    data = call_topapi(access_token, 'extcontact/update', 'POST', contact=contact)
    return data


@dingtalk_resp
def delete_corp_ext(access_token, user_id: int):
    """
    删除外部联系人
    :return:
    """
    data = call_topapi(access_token, 'extcontact/delete', 'POST', user_id=user_id)
    return data
