#!/usr/bin/env python
# -*- coding": "utf-8 -*-
# qw @ 2017-12-11 12:57:46
import requests
import copy
import json
import random
import re
import logging
import traceback
import socket
import struct


#logging.basicConfig(level=logging.DEBUG)

class generate_cookies(object):
    def __init__(self,):
        self.headers = {
            #"Host": "passport.weibo.com",
            "Connection": "keep-alive",
            #"Content-Length": "580",
            "Pragma": "no-cache",
            "Cache-Control": "no-cache",
            "Origin": "https://passport.weibo.com",
            "Referer": "http://s.weibo.com/weibo/cash&Refer=STopic_box",
            #"If-Modified-Since": "0",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6)" +\
                " AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
            "Content-Type": "application/x-www-form-urlencoded",
            "Accept": "*/*",
            #"Referer": "https://passport.weibo.com/visitor/visitor" +\
            #    "?entry=miniblog&a=enter" +\
            #    "&url=https%3A%2F%2Fweibo.com%2Ftv%2Fv%2FFxTWzj4PW%3Ffrom%3Dtech" +\
            #    "&domain=.weibo.com&ua=php-sso_sdk_client-0.6.23&_rand=1512967862.0547",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "en,zh-CN;q=0.9,zh;q=0.8,ja;q=0.7,zh-TW;q=0.6,en-US;q=0.5",
            #"Cookie": "SINAGLOBAL=5240597717720.268.1506667412712; SCF=AvYIbbUZ1Vl6HBO4sC-H3OJlvhvxnzlAaeUpHvg2X9rXK9IQfdsl-mz2JGOr20dWFA8b4L2O_KmSfynIxkAE_ZU.; SUHB=0A04M0X995CPxp; SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9WFxYOLPzbimrmd5kYReDnHd; UOR=www.baidu.com,vdisk.weibo.com,fuliba.net; SUB=_2AkMtllJcf8NxqwJRmPgXz2njb4p1zwvEieKbyqOHJRMxHRl-yj83qkUFtRB6BhZ8snmJvUIZE-eP17-WfP9N-x7mlOG5; _s_tentry=-; Apache=5983775453128.07.1532175148905; ULV=1532175148914:11:1:1:5983775453128.07.1532175148905:1526609583127; WBStorage=5548c0baa42e6f3d|undefined; SWB=usrmdinst_0"
                #"UM_distinctid=15ecc603b9ab16-09a2d08fd8bba7-31627c01-13c680-15ecc603b9c7fd" +\
                #"; SINAGLOBAL=5240597717720.268.1506667412712" +\
                #"; UOR=www.baidu.com,vdisk.weibo.com,www.expreview.com",
            }
        logging.debug("original headers :%s " % self.headers)
        logging.debug("original headers key:%s" % self.headers.keys())
        original_cookie = self.headers.get("Cookie", "")
        logging.debug("original cookie:%s" % original_cookie)
        cookies = self.generate()
        logging.debug("new cookie:%s" % cookies)
        self.headers["Cookie"] = original_cookie + cookies
        logging.debug("init headers:%s" % self.headers)

    def get_tid(self, ):
        url = "https://passport.weibo.com/visitor/genvisitor"
        data = {
            "cb":"gen_callback", 
                "fp":{
                    "os":"2",
                    "browser":"Chrome61,0,3163,100",
                    "fonts":"undefined",
                    "screenInfo":"1440*900*24",
                    "plugins":"Portable Document Format::internal-pdf-viewer::Chrome PDF Plugin|::mhjfbmdgcfjbbpaeojofohoefgiehjai::Chrome PDF Viewer|::internal-nacl-plugin::Native Client|Enables Widevine licenses for playback of HTML audio/video content. (version\": \"1.4.8.1008)::widevinecdmadapter.plugin::Widevine Content Decryption Module"
                    }
                } 
        res = requests.post(url, headers=self.headers, data=data)
        res_dict = re.findall("(\{[\s\S]*\})", res.content)
        if res_dict:
            try:
                return json.loads(res_dict[0]).get("data", {}).get("tid", None)
            except:
                traceback.print_exc()
                return None
        else:
            return None

    def generate(self,):
        while 1:
            if self.headers.has_key("Cookie"):
                del(self.headers["Cookie"])
            #if self.headers.has_key("Referer"):
            #    del(self.headers["Referer"])
            self.headers["Host"] = "passport.weibo.com"
            new_pri = socket.inet_ntoa(struct.pack('>I', random.randint(1, 0xffffffff)))
            self.headers["X-Forwarded-For"] = new_pri
            self.headers['X-real-IP'] = new_pri
    
            url = "https://weibo.com"
            tid = self.get_tid()
            confidence = "095"
            url = "https://passport.weibo.com/visitor/visitor" +\
                "?a=incarnate&t=%s&w=2&c=%s&gc=&cb=cross_domain&from=weibo&_rand=%s"%\
                    (tid, confidence, random.random())
            res = requests.get(url = url, headers={}, cookies={})
            #logging.debug("response headers:%s" % res.headers)
            cookies =  res.headers.get("Set-Cookie", None)
            if cookies and cookies.startswith("SUB="):
                return cookies

    def test_get(self):
        url = "https://weibo.com/tv/v/FxTWzj4PW?from=tech"
        url = "https://weibo.com/tv/world"
        cookies = self.generate()
        headers = copy.deepcopy(self.headers)
        headers["Cookie"] = cookies
        #headers["Upgrade-Insecure-Requests"] = "1"
        headers["Host"] = "weibo.com"
        res = requests.get(url=url, headers=headers,)
        return res.content

if __name__ == "__main__":
    try:
        #print generate_cookies().test_get()
        print generate_cookies().generate()
    except:
        traceback.print_exc()
        pass

