#!/usr/bin/env python
# -*- coding: utf-8 -*-
# qw @ 2018-07-21 23:05:07

import sys
sys.path.append("./")

from apps.request_pin.request_pin import request_pin
from apps.identify_pin.identify_pin import identify_pin
from apps.generate_cookies.generate_cookies import generate_cookies
from apps.write_png.write_png import write_png

if __name__ == "__main__":
    png_code, png_content, headers = request_pin()
    file_path = "./image/%s.png" % png_code
    write_code = write_png(file_path, png_content)
    manual_code = raw_input("new identify code:%s, please input that code: " % file_path)
    identify_status, identify_response = identify_pin(headers, manual_code)
    print "file_path:%s, manual_code:%s, auth_status:%s" % (file_path, manual_code, identify_status)

