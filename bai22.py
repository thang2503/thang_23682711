# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 22:38:03 2024

@author: ACER
"""

a = float(input("Nhập số a:"))
b = float(input("Nhập số b:"))
if a != 0:
    print("Phương trình có nghiệm x=" , -b/a)
else:
    if b != 0:
        print("Phương trình vô nghiệm")
    else:
        print("Phương trình vô số nghiệm")
            