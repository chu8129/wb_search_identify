#!/usr/bin/env python
# -*- coding: utf-8 -*-
# qw @ 2018-07-21 20:49:35

import sys
sys.path.append("./")

import re
import time
import requests

from apps.generate_cookies.generate_cookies import generate_cookies

import logging

def request_pin(headers=None):
    url = "http://s.weibo.com/ajax/pincode/pin?type=sass" + str(int(time.time()*1000))
    logging.debug("request url:%s" % url)
    if headers == None:
        req = generate_cookies()
        headers = req.headers
    headers["Accept"] = "image/webp,image/apng,image/*,*/*;q=0.8"
    headers["Host"] = "s.weibo.com"
    #headers["Referer"] = "http://s.weibo.com/weibo/cash&Refer=STopic_box"
    logging.debug("request headers:%s" % headers)
    
    res = requests.get(url, headers=headers)
    #logging.debug(res.content)
    image_code = None
    image_path = None
    if res:
        new_cookies = res.headers.get("Set-Cookie", None)
        logging.debug("response cookies:%s" % new_cookies)
        if new_cookies:
            image_code_list = re.findall("ULOGIN_IMG=(\d+)", new_cookies) 
            logging.debug("re match img code:%s" % image_code_list)
            if image_code_list:
                image_code = image_code_list[0]
                headers["Cookie"] += "; ULOGIN_IMG=%s" % image_code  
    #            image_path = "./image/%s.png"%image_code
    #    if image_code and image_path:
    #        with open(image_path, "wb") as fw:
    #            fw.write(res.content)
    return image_code, res.content, headers

if __name__ == "__main__":
    print request_pin()
