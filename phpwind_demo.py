#!/usr/bin/env python
# encoding: utf-8
# @author:lrh
# @file:论坛注册账号
# @time:2020/8/3 17:56

import requests
import re

session = requests.session()
hosts = 'http://47.107.178.45'

#1.进入论坛首页
res01 = session.get(url=hosts + '/phpwind/')
body01 = res01.content.decode('utf-8')
csrf_token = re.findall('name="csrf_token" value="(.+?)"',body01)[0];

# 2.注册账号
get_params = {
    "m":"u",
    "c":"register"
}
res02 = session.get(url=hosts + '/phpwind/index.php',
                    params = get_params
                    )
# print(res02.content.decode('utf-8'))

# 3.填写信息
get_params = {
    "m": "u",
    "c": "register",
    "a":"dorun"
}
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:68.0) Gecko/20100101 Firefox/68.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
    "Accept-Encoding": "gzip, deflate",
    "Content-Type": "application/x-www-form-urlencoded",
    "X-Requested-With":"XMLHttpRequest"
}
post_params = {
    "username":"liu3",
    "password":"123456",
    "repassword":"123456",
    "email":"liu3@qq.com",
    "csrf_token":csrf_token

}
res03 = session.post(url=hosts+'/phpwind/index.php',
                     params = get_params,
                     headers = headers,
                     data= post_params
                     )
print(res03.content.decode('utf-8'))

