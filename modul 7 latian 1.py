# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 14:17:44 2022

@author: fariz
"""
def penutup():
    print('''terimakasih telah menggunakan program saya.
ig:@alfarizqiwira''')
def pemilih():
    o=1
    while o==1:
        angka=(input('masukan angka: '))
        h=0    
        if angka == '':
            o=2
        elif int(angka) == 1:
            print('bukan bilangan prima')
        elif int(angka) > 0:
            for i in range (2,int(angka)):
                bil = int(angka)%i
                if bil == 0:
                    h=h+1
                elif bil > 0:
                    h=h
            if h == 0:
                print('bilangan prima')
            elif h > 0:            
                print('bukan bilangan prima')
        elif int(angka) <= 0:
            print('bilangan harus diatas 0 (positif)')
        elif angka == '':
            o=2
print('program penentuan bilangan prima')
pemilih()
penutup()
