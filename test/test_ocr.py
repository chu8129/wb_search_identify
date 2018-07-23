#!/usr/bin/env python
# -*- coding: utf-8 -*-
# qw @ 2018-07-23 23:20:38

import sys
sys.path.append("./")

from apps.ocr.ocr import ocr

if __name__ == "__main__":
    print ocr(sys.argv[1])
