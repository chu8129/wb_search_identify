#!/usr/bin/env python
# -*- coding: utf-8 -*-
# qw @ 2018-07-23 23:17:20

import sys
sys.path.append("./")

import os
import pytesseract
import multiprocessing
from PIL import Image

def twovalue(image, G):
    t2val = {}
    for y in xrange(0,image.size[1]):
        for x in xrange(0,image.size[0]):
            g = image.getpixel((x,y))
            if g > G:
                t2val[(x,y)] = 1
            else:
                t2val[(x,y)] = 0
    return t2val




averageinterferencethrehold=90

#筛选验证码，codetype是指取白色255还是黑色0，threhold是阀值
def directthrehold(img,codetype=255,threhold=-1):
        if threhold == -1:
                threhold=50 if codetype==255 else 200
        img=img.convert("L")
        pixdata=img.load()
        (Width,Height) = img.size
        for i in xrange(Width):
                for j in xrange(Height):
                        if pixdata[i,j]>threhold:
                                pixdata[i,j]=255 if codetype==255 else 0
                        else:
                                pixdata[i,j]=0 if codetype==255 else 255
        return img
#利用3*3窗口调整颜色，当然可以将其变化为0/255；
def averagevalue(img):
        img=img.convert("L")
        pixdata=img.load()
        result=img.copy()
        resultpixdata=result.load()
        (Width,Height) = img.size
        for i in xrange(Width):
                for j in xrange(Height):
                        xlabel=[1, 0, -1, 0, 1, -1, 1, -1]
                        ylabel=[0, 1, 0, -1, -1, 1, 1, -1]
                        data=[]
                        for k in xrange(8):
                                if 0<i+xlabel[k]<Width and 0<i+ylabel[k]<Height:
                                        data.append(pixdata[i+xlabel[k],i+ylabel[k]])
                        data.sort()
                        if len(data)>0:
                                midvalue=sum(data)/len(data)
                        else:
                                midvalue=0
                        if abs(pixdata[i,j] - midvalue)>averageinterferencethrehold:
                                resultpixdata[i,j]=pixdata[i,j]
                        else:
                                resultpixdata[i,j]=max(midvalue,pixdata[i,j])
        return result

def ocr(file_path):
    abs_file_path = os.path.abspath(file_path)
    #subprocess.Popen()
    img = Image.open(file_path)
    img = averagevalue(img)
    return pytesseract.image_to_string(img, lang="eng")

if __name__=="__main__":
        img=Image.open(sys.argv[1])
        img.show()
        img=img.convert('L')
        #img.show()
#       img1=directthrehold(img)
#       img1.show()
        averagevalue(img).show()
        #directthrehold(averagevalue(img),0).show()
#       directthrehold(img2).show()
