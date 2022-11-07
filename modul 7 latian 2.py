# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 09:36:26 2022

@author: fariz
"""

def fungsi (a,b,c,d):
    if a == b:
        print(d,c)
i=1 
while i == 1:
    angka=input('masukan angka: ')
    if angka == '':
        i=0
    elif (angka=='11')or(angka=='12')or(angka=='13'):
        print(angka,'th')
    else:
        itung=int(angka)%10
        fungsi(itung, 1, 'st',angka)
        fungsi(itung, 2, 'nd',angka)
        fungsi(itung, 3, 'rd',angka)
        fungsi(itung, 0, "th",angka)
        fungsi(itung, 4, 'th',angka)
        fungsi(itung, 5, 'th',angka)
        fungsi(itung, 6, 'th',angka)
        fungsi(itung, 7, 'th',angka)
        fungsi(itung, 8, 'th',angka)
        fungsi(itung, 9, 'th',angka)
print('''
terima kasih telah menggunakan program saya
ig: alfarizqiwira''')