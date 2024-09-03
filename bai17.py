# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 22:34:25 2024

@author: ACER
"""

a = int(input("Nhập số nguyên 1: "))
b = int(input("Nhập số nguyên 2: "))
c = int(input("Nhập số nguyên 3: "))
so_lon_nhat = max(a, b, c)
so_nho_nhat = min(a, b, c)
print("số lớn nhất là: " , so_lon_nhat)
print("số nhỏ nhất là: " , so_nho_nhat)