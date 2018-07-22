#!/usr/bin/env python
# -*- coding: utf-8 -*-
# qw @ 2018-07-21 23:11:22

import sys
sys.path.append("./")

def write_png(file_path, content):
    with open(file_path, "wb") as fw:
        fw.write(content)
    return 1
