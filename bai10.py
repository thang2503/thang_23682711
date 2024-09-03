# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 22:18:24 2024

@author: ACER
"""

so_xe = int(input("Nhập số xe gồm 4 chữ số: "))
so_xe = str(so_xe) 
a = 0
for i in range(len(so_xe)) :
    a = int(so_xe[i])
print("số nút của số xe là:" , a % 10)