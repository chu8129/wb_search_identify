#!/usr/bin/env python
# -*- coding: utf-8 -*-
# qw @ 2018-07-21 22:41:26

import sys
sys.path.append("./")


import re
import time
import requests
import json
 
import logging
 
def identify_pin(headers, identify_code):
    url = "http://s.weibo.com/ajax/pincode/verified?__rnd=" + str(int(time.time()*1000))
    logging.debug("request url:%s" % url)
    logging.debug("original headers:%s" % headers)

    headers["Accept"] = "*/*"
    headers["Host"] = "s.weibo.com"
    #headers["Referer"] = "http://s.weibo.com/weibo/cash&Refer=STopic_box"
    headers["X-Requested-With"] = "XMLHttpRequest"
    headers["Origin"] = "http://s.weibo.com"
    headers["Accept-Encoding"] = "gzip, deflate"

    new_headers  = {}
    new_headers["Content-Type"] = headers["Content-Type"]
    new_headers["Referer"] = headers["Referer"]  
    new_headers["Accept"] = headers["Accept"]
    new_headers["User-Agent"] = headers["User-Agent"]
    new_headers["Origin"] = headers["Origin"]
    new_headers["X-Requested-With"] = headers["X-Requested-With"]
    headers = new_headers 

    data = {
            "secode":identify_code,
            "type":"sass",
            "pageid":"weibo",
            "_t":"0"
        }

    for k,v in headers.iteritems():
        logging.debug("identify headers,%s    %s" % (k, v))

    logging.debug("identify post data:%s" % data)
    res = requests.post(url, headers=headers, data=data)
    logging.debug("post identify code response:%s" % res.content)
    if res.content:
        try:
            msg = json.loads(res.content)
            logging.debug("response msg:%s" % msg.get("msg"))
        except Exception as e:
            logging.error(str(e), exc_info=True)
    auth_code = 0
    logging.debug("code:%s" % json.loads(res.content).get("code", None))
    if res.content and str(json.loads(res.content).get("code", None)) in ["100028","100001"]:
        auth_code = 0
    else:
        auth_code = 1
    return auth_code, res.content


