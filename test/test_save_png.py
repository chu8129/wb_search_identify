#!/usr/bin/env python
# -*- coding: utf-8 -*-
# qw @ 2018-07-21 23:02:46

import sys
sys.path.append("./")

from apps.request_pin.request_pin import request_pin

if __name__ == "__main__":
    png_code, png_content, headers = request_pin()

    with open("./image/%s.png" % png_code, "wb") as fw:
        fw.write(png_content)
