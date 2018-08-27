#!/usr/bin/env python
# -*- coding: utf-8 -*-
# qw @ 2018-07-24 00:04:48

import sys
sys.path.append("./")

from apps.mark_image.mark_image import mark_image

if __name__ == "__main__":
    with open("result.txt", "a+") as fw:
        for i in xrange(0, int(sys.argv[1])):
            file_path, code, status =  mark_image()
            fw.write(",".join([file_path, code, str(status)]) + "\n")
