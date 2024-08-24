# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 23:04:12 2024

@author: ASUS
"""

a=int(input("Nhap gio:"))
b=int(input("Nhap phut:"))
c=int(input("Nhap giay:"))
if a>=0 and a<24 and b>=0 and b<60 and c>=0 and c<60:
    print("Bay gio la:",a,"gio",b,"phut",c,"giay")
    x=a*3600
    y=b*60
    print("Tong so giay dua theo so gio tren :",x+y+c,"")
else:
    print("Nhap sai!Moi nhap lai")