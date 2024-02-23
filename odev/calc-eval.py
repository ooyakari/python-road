#Öncelikle programımızın en başına kullanım kılavuzuna benzer bir metin yerleştirdik ve bu metni print() fonksiyonu yardımıyla ekrana bastık.
#Eval fonksiyonunun dezavantaji var,  islemi sordugumda kullanici oraya sayi yerine komut girebiliyor. örnek olarak, islem sorusuna print("Merhaba") yazarsam, cikti alabiliyorum. Böylece sisteme girebilir, verileri alip görebilirim.
 

print("""
Hesap makinesi.
İşlemler:
    +   toplama
    -   çıkarma
    *   çarpma
    /   bölme
Yapmak istediğiniz işlemi (5 * 10) gibi yazarak enter a basin.))
""")

#Input yoluyla kullanicidan aldigimiz degeri 'veri' degiskenine atadik.
veri = input("İşleminiz: ")

#Ardından, kullanıcıdan gelen veriyi eval() fonksiyonu yardımıyla değerlendirmeye tabi tutuyoruz. Yani kullanıcının girdiği komutları işleme sokuyoruz. Örneğin, kullanıcı 46 / 2 gibi birverigirdiyse,bizeval()fonksiyonuyardımıylabu46 / 2komutunuişletiyoruz.Buişlemin sonucunu da hesap adlı başka bir değişken içinde depoluyoruz.

hesap = eval(veri)

#Son olarak sonucu ekrana print ile yazdiriyoruz.
print("Sonuc :", hesap)