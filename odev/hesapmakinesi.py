#Hesap Makinesi Uygulamasi
#Neden int yerine float kullandim ?
#Float() = Bu fonksiyonu, sayıları veya karakter dizilerini kayan noktalı sayıya dönüştürmek için kullanıyoruz.
#Aslinda ilk olarak int kullanmistim. Fakat islem sirasinda küsuratli sayi girdigimde programin cöktügünü gördüm. Bu cökmeyi engellemek icin int yerine float kullandim.



#While = Döngü olusturarak, uygulamanin sürekli calismasini sagladim. Böylece, islem her bittiginde tekrar basa dönerek baska islem yapip yapmayacagini soruyor.
while True:
    #Burada print \t ile baslik verip, altina kullanicidan yapmak istedigi islemi ögreniyorum.
    print("""\t--------- Hesap Makinesi ----------- """)
    islem = input("""Yapmak istediginiz islemi seciniz:(Cikmak icin C harfine basiniz)
(Toplama : +, Cikarma : - , Bölme : / , Carpma : x)  """)
    
    #Kullanici c harfine basarsa, if islem == 'c' komutuyla islemi sonlandiriyorum. 
    if islem == 'c':
        print("Çıkılıyor...")
        quit()

    #Kullanici +,-,/,x islemlerinden birini secerse, elif komutlariyla islemleri yaptiriyorum.
    elif islem == "+":
        firstNum = float(input("Ilk sayinizi giriniz: "))
        secNum = float(input("Ikinci sayiyi giriniz: "))
        print("Toplama isleminizin sonucu : ", firstNum, "+", secNum, "=", (firstNum+secNum))
    elif islem == "-":
        firstNum = float(input("Ilk sayinizi giriniz: "))
        secNum = float(input("Ikinci sayiyi giriniz: "))
        print("Cikarma isleminizin sonucu : ", firstNum, "-", secNum, "=", (firstNum-secNum))
    elif islem == "/":
        firstNum = float(input("Ilk sayinizi giriniz: "))
        secNum = float(input("Ikinci sayiyi giriniz: "))
        print("Bölme isleminizin sonucu :", firstNum, "/", secNum, "=", (firstNum/secNum))
    elif islem == "x":
        firstNum = float(input("Ilk sayinizi giriniz: "))
        secNum = float(input("Ikinci sayiyi giriniz: "))
        print("Carpma isleminizin sonucu :", firstNum, "x", secNum, "=", (firstNum*secNum))

    #Else komutu ile, kullanici gecersiz komut girdiginde uyariyorum.
    else:
        print("Gecersiz islem, tekrar deneyiniz")
