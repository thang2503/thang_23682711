# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 22:30:54 2024

@author: ACER
"""

ngay = int(input("Nhập ngày sinh:"))
thang = int(input("Nhập tháng sinh:"))
nam = int(input("Nhập năm sinh:"))
print(f"{ngay}/{thang}/{nam}")
print(f"{ngay}/{thang}/{str(nam)[-2:]}")
print(f"{nam}/{ngay}/{thang}")
ngay , thang , nam = map(int , input("Nhập theo định dạng ngày/tháng/năm:").split('/'))
print(f"{ngay}/{thang}/{nam}")
print(f"{ngay}/{thang}/{str(nam)[-2:]}")
print(f"{nam}/{ngay}/{thang}")