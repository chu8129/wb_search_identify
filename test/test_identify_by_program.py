#!/usr/bin/env python
# -*- coding: utf-8 -*-
# qw @ 2018-07-24 00:04:48

import sys
sys.path.append("./")

from apps.mark_image.mark_image import mark_image

if __name__ == "__main__":
    file_path, code, status =  mark_image()
    with open("result.txt", "wa") as fw:
        fw.write(",".join([file_path, code, str(status)]) + "\n")
