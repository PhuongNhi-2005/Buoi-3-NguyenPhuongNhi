# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 22:59:12 2024

@author: ASUS
"""

a=int(input("Nhap so nguyen N co 2 chu so:"))
if a>=10 and a<=99:
    x=a//10
    y=a%10
    print("Tong cua 2 chu so la:",x+y)
else:
    print("Nhap sai!Moi nhap lai")