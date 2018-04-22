# -*- coding:utf8 -*-

import urllib.request
import re
import time

headers = {
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'User-Agent': 'Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
    'Hosts': 'hm.baidu.com',
    'Referer': 'http://www.xicidaili.com/nn',
    'Connection': 'keep-alive'
}

# 指定爬取范围（这里是第1~500页）
for i in range(1,500):

    url = 'http://www.xicidaili.com/nn/' + str(i)
    request = urllib.request.Request(url, headers=headers)
    reponse = urllib.request.urlopen(request).read().decode('utf-8')

    # 提取ip和端口
    ip_list = re.findall("(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}).*?(\d{2,6})", reponse, re.S)

    # 将提取的ip和端口写入文件
    f = open("./ip.txt","a+")
    for li in ip_list:
        ip = li[0] + ':' + li[1] + '\n'
        print (ip)
        f.write(ip)

    time.sleep(1)       # 每爬取一页暂停1秒