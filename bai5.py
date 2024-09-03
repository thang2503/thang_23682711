# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 22:04:19 2024

@author: ACER
"""

thoi_gian=input("Nhập thời gian theo định dạng hh:mm:ss:")
hh=int(thoi_gian [0:2])
mm=int(thoi_gian [3:5])
ss=int(thoi_gian [6:8])
tong_giay = hh * 3600 + mm * 60 + ss
print("Tổng số giây: " , tong_giay)