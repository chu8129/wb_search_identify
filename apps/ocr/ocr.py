#!/usr/bin/env python
# -*- coding: utf-8 -*-
# qw @ 2018-07-23 23:17:20

import sys
sys.path.append("./")

import os
import pytesseract
import multiprocessing
from PIL import Image

def ocr(file_path):
    abs_file_path = os.path.abspath(file_path)
    #subprocess.Popen()
    return pytesseract.image_to_string(Image.open(file_path))
