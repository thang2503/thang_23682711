# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 22:15:52 2024

@author: ACER
"""

print("============ MENU ============")
print("1.Hu tieu")
print("2.Chao long")
print("3.Banh canh")
print("4.Bun rieu")
print("5.Pho bo")
print("============================")
a = int(input("Moi nhap lua chon: "))
print("============================")
if a == 1:
    print("Hu tieu")
elif a == 2:
    print("Chao long")
elif a == 3:
    print("Banh canh")
elif a == 4:
    print("Bun rieu")
elif a == 5:
    print("Bun bo")
else:
    print("Khong co mon trong menu")