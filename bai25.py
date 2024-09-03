# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 22:40:08 2024

@author: ACER
"""
a = input("Nhập 1 chữ cái: ")
if a.islower():
    a = a.upper()
    print("Chữ cái thường đổi thành chữ cái hoa: " , a)
elif a.isupper():
    a = a.lower()
    print("Chữ cái hoa đổi thành chữ cái thường: " , a)
else:
    print("Không xác định")
