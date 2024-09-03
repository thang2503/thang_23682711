# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 22:38:44 2024

@author: ACER
"""

import math
a = float(input("Nhập số a: "))
b = float(input("Nhập số b: "))
c = float(input("Nhập số c: "))
delta = b**2-4*a*c
if delta == 0:
    x = -b / (2*a)
    print("Vậy phương trình có nghiệm kép là: " , x)
elif delta < 0:
    print("Vậy phương trình vô nghiệm")
else:
    x1 = -b + math.sqrt(delta) / (2*a)
    x2 = -b - math.sqrt(delta) / (2*a)
    print("Vậy phương trình có hai nghiệm phân biệt là: ")
    print("x1:" , x1 , "x2:" , x2)