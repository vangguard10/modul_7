# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 14:17:44 2022

@author: fariz
"""
def penutup():
    print('''terimakasih telah menggunakan program saya.
ig:@alfarizqiwira''')
def pemilih():
    angka=int(input('masukan angka: '))
    h=0
    if angka == 1:
        print('bukan bilangan prima')
    elif angka in range(2,4):
        print('bilangan prima')
    elif angka > 0:
        i=2
        while i in range(2,angka):
            bil = angka%i
            if bil == 0:
                h=h+1
                i+=1
            elif bil > 0:
                h=h
                i+=1
        
        if h == 0:
            print('bilangan prima')
        elif h > 0:
        
            print('bukan bilangan prima')
    elif angka <= 0:
        print('bilangan harus diatas 0 (positif)')
 
o=1
while o==1:
    print('program penentuan bilangan prima')
    pemilih()
         
    b=1
    while b == 1:
        jwbn=input('apakah ingin mengulanginya lagi?[Y/N]')
        if jwbn.upper() =='Y':
            b=0
            o=1
        elif jwbn.upper() =='N':
            b=0
            o=0
        else:
            b=1
penutup()
