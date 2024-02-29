
# def komutu ile fonksion olusturuyoruz. örnek : def degiskenadi(a, b, c) gibi.

#örnegin hesap makinesi yaparken def fonksionlarina degisken tanimlayip, sonra if ile degiskenlere isletiyoruz.
#return ile islemi geri döndürüyoruz..
#result degiskeni olusturarak, tek satirlik kod ile tüm sonuclara result yazdiriyoruz.
#lambda ile if kullanmak yerine, tek tek secenekleri siralayarak secimleri def e gönderebiliyoruz. 
#len = length





def toplama(a, b):
    return a+b

def cikarma(a, b):
    return a-b

def bolme(a, b):
    return a/b

def carpma(a, b):
    return a*b

def displayResult(op):
    print("Result :", op)

operations ={
    1: lambda a,b : a+b,
    2: lambda a,b : a-b,
    3: lambda a,b : a/b,
    4: lambda a,b : a*b,
}
islem = int(input(""" 
    Yapmak istediginiz islemi seciniz: 
        1- Toplama
        2- Cikarma 
        3- Bölme
        4- Carpma 

    Isleminiz: """))
if islem > len(operations):
    print("Hatali islem")
    quit()

num1 = int(input("Birinci sayiyi giriniz: "))
num2 = int(input("ikinci sayiyi giriniz: "))
result = operations[islem](num1, num2)
displayResult(result)

exit()

if islem =='1':
    result = toplama(num1, num2)
    
if islem =='2':
    result = cikarma(num1, num2)
    
if islem =='3':
    result = bolme(num1, num2)
    
if islem =='4':
    result = carpma(num1, num2)
displayResult(result)