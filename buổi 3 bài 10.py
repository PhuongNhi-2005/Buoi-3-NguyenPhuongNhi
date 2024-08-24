# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 23:06:11 2024

@author: ASUS
"""

print(" =========== MENU ============ ")
print("        1. Hủ tiếu")
print("        2. Cháo lòng")
print("        3. Bánh canh")
print("        4. Bún riêu")
print("        5. Phở bò")
print(" ============================== ")
menu = ["1","2","3","4","5","hủ tiếu","cháo lòng","bánh canh", "bún riêu","phở bò"]
luachon = input(" Mời nhập lựa chọn: ")
if luachon in menu: 
   print(" ============================== ")
else:
    print("Món bạn chọn không có trong menu. Vui lòng nhập lại !")