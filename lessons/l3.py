# def komutu ile fonkison olusturuyoruz. örnek : def degiskenadi(num1, num2) gibi.

#örnegin hesap makinesi yaparken def ile degisken tanimlayip, sonra if ile degiskenlere isletiyoruz.

islem = input(""" 
    Yapmak istediginiz islemi seciniz: 
        1- Toplama
        2- Cikarma 
        3- Bölme
        4- Carpma 

    Isleminiz: """)


def toplama(a, b):
    displayResult((a+b))

def cikarma(a, b):
    displayResult((a-b))

def bolme(a, b):
    displayResult((a/b))

def carpma(a, b):
    displayResult((a*b))

def displayResult(op):
    print("Result :", op)

num1 = int(input("Birinci sayiyi giriniz: "))
num2 = int(input("ikinci sayiyi giriniz: "))


if islem =='1':
    toplama(num1, num2)
if islem =='2':
    cikarma(num1, num2)
if islem =='3':
    bolme(num1, num2)
if islem =='4':
    carpma(num1, num2)