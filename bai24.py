# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 22:39:24 2024

@author: ACER
"""

gio = int(input("Nhập giờ: "))
phut = int(input("Nhập phút: "))
giay = int(input("Nhập giây: "))
if 0 <= gio < 24 and 0 <= phut < 60 and 0 <= giay < 60:
    print("giờ, phút, giây hợp lệ")
else:
    print("giờ, phút, giây không hợp lệ")