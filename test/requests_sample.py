#!/usr/bin/env python
# -*- coding: utf-8 -*-
# qw @ 2018-08-28 01:18:53

import sys
sys.path.append("./")
import time

headers = {
"Accept":"*/*",
"Accept-Encoding":"gzip, deflate",
"Accept-Language":"en,zh-CN;q=0.9,zh;q=0.8,ja;q=0.7,zh-TW;q=0.6,en-US;q=0.5",
"Cache-Control":"no-cache",
"Connection":"keep-alive",
"Content-Length":"39",
"Content-Type":"application/x-www-form-urlencoded",
"Cookie":"WBStorage=e8781eb7dee3fd7f|undefined; _s_tentry=-; Apache=5698283981437.311.1535390219139; SINAGLOBAL=5698283981437.311.1535390219139; ULV=1535390219448:1:1:1:5698283981437.311.1535390219139:; SWB=usrmdinst_22",
"Host":"s.weibo.com",
"Origin":"http://s.weibo.com",
"Pragma":"no-cache",
"Referer":"http://s.weibo.com/weibo/%25E6%25B5%258B%25E8%25AF%2595&Refer=STopic_box",
"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
"X-Requested-With":"XMLHttpRequest",
}

data = {
            "secode": "",
            "type":"sass",
            "pageid":"weibo",
            "_t":"0"
        }

import requests

headers["Cookie"] += "; ULOGIN_IMG=%s"%sys.argv[1]
data["secode"] = sys.argv[2]

import json
print json.dumps(headers, indent=4)
print data

print requests.post(url = "http://s.weibo.com/ajax/pincode/verified?__rnd=" + str(int(time.time()*1000)), headers=headers, data=data).content
