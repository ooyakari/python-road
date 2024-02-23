#1 - Print -
#2 - Variables - (Degiskenler)
#3 - Comments - (Yorum satirlari)


print('usiv') #() isareti bunun bir fonksion oldugunu belirtir.

#End parametresi

print('end parametresi satiri devam ettiriyor, \n ise yeni satir aciyor', end='.\n')
print('ikinci satir')

#Input ve if olusturma
email = input("E-Mail Adresiniz:")
if email:
    print("Tesekkürler")
else:
    print('Email adresinizi girmediniz')
password = input("Password giriniz:" )
if password:
    print('Password basariyla girildi')
else:
    print('Password girmediniz')

#File parametresi -> Örnek olarak errors log gösterilebilir. Ciktiyi direkt dosyaya yazar.
#Mode="w" (sadece write demek)
errors = open(file="errors.txt", mode="w")
print('File parametresi', file=errors)

#Kullanici girisi kontrolü projesi
#1. Create Form 
print(email, file=errors)
print(password, file=errors)
#2. Create password and Email input
print('Email ve password girildi', file=errors)
#3. Create Submit button
print('Butona basti', file=errors)

errors.close()

#Degisken tanimlamak icin örnek : yas=19 ve bu degiskeni yazdirmak icin {yas} yapmak yeterli. Böylece tanimladigin degeri ekrana yazdirabilirsin.


yas = 19


print(yas)
