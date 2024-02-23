#Tek tirnak ve cift tirnak arasinda fark var.
#Tek tirnak ' : string olarak degerlendirilir. Yani yazi olarak. örnek: print('YAZI)
#Cift tirnak ise 
#Print icerisine degiskeni cift tirnak icerisinde de yazabiliriz. örnek : print(" " + degiskenadi + " ")
#tek satirda yazip, alt satirlara siralamasini istiyorsak \n ekleriz arasina.
#print(f") string icin kullanilir.
# \t = taba basmak anlaminda, satirda bi tab bosluk birakir.

# \n ve \t gibi isaretlere ESCAPE denir. Escape kisaltmalari birden fazla var. Yazbel pdf kitabinda 111. sayfada mevcut.


degisken1 = "test"
degisken2 = "deneme"
print(f" {degisken1} \n {degisken2}") 

#INPUTLAR
#degisken basina int() ekleyerek sayi oldugunu belirtebiliriz. Böylece yazi yazilamaz input alanina.
#age degiskenini print ederken, yazi ve sayi toplanamayacagi icin virgül ile ayiririm.

email = input("Email adresiniz nedir?: ")
password = input("Sifre nedir ?: ")
age = int(input("Yasiniz nedir?: "))
print("E-Mail\t : " + email + "\nSifre\t: " + password + "Yasiniz\t : " , age)

#TYPE komutu degiskenin türünü belirtir. Örnek : print(type(age)) yazarsan, ekrana integer oldugunu yazdirir.

