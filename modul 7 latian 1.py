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
            i=2
            while i in range(2,int(angka)):
                bil = int(angka)%i
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
        elif int(angka) <= 0:
            print('bilangan harus diatas 0 (positif)')
        elif angka == '':
            o=2
print('program penentuan bilangan prima')
pemilih()
penutup()
