#!/usr/bin/env python
# -*- coding: utf-8 -*-
# qw @ 2018-07-23 23:59:49

import sys
sys.path.append("./")

import os
import re

from apps.request_pin.request_pin import request_pin
from apps.write_png.write_png import write_png
from apps.ocr.ocr import ocr
from apps.identify_pin.identify_pin import identify_pin

def mark_image():
    identify_status = 0
    png_code, png_content, headers = request_pin()
    file_path = os.path.abspath("./image/%s.png" % png_code)
    write_code = write_png(file_path, png_content)
    manual_code = re.sub("[^a-zA-Z0-9]", "", ocr(file_path))[:4]
    if manual_code.isalnum() and len(manual_code) == 4:
        identify_status, identify_response = identify_pin(headers, manual_code)
    return file_path, manual_code, identify_status
