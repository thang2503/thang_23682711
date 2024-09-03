# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 22:11:33 2024

@author: ACER
"""

can_nang=float(input("Nhập cân nặng (kg): "))
chieu_cao=float(input("Nhập chiều cao (m): "))
BMI=can_nang / chieu_cao**2
print("Số đo kiểm tra sức khỏe BMI là: " , BMI)