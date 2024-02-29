#Tas, Kagit & Makas oyunu

#1.adimda bilgisayarin kullanacagi random sayilari üretmek icin random modülünü projeye import ediyorum.

import random

#2. adimda kullanicidan secim yapmasini istedigim ve eger istedigim secimi yapmazsa uyaracagim bir input fonksionu olusturuyorum.

def oyuncu():
    while True:
        oyuncusecimi = input("Tas icin 't', Kagit icin 'k' Makas icin 'm' harfine basiniz: ").lower() #Burada girilen harfleri kücültmesi icin lover() kullandim.
        if oyuncusecimi in ('t', 'k', 'm'):
            return oyuncusecimi
        else:
            print("Gecersiz islem yaptiniz. Lütfen dogru secimi yapiniz.")

#3. adimda bilgisayarsecimi adinda bir fonksion olusturarak, bilgisayara köseli parantez icerisinde belirledigim harfler arasindan random secim yaptiriyorum. 
            
def bilgisayar():
    return random.choice(['t', 'k', 'm'])

#4. adimda ise sonuc adinda bir fonksion olusturarak, sonucu hesaplatiyorum.

def sonuc(oyuncu, bilgisayar):
    
    if oyuncu == bilgisayar:
        return "Berabere!"
    elif (oyuncu == 't' and bilgisayar == 'm') or (oyuncu == 'k' and bilgisayar == 't') or (oyuncu == 'm' and bilgisayar == 'k'):
        return "Tebrikler! Kazandiniz!"
    else:
        return "Kaybettiniz!"
    
#5. adimda ise main adinda ana fonksionu while döngüsü icerisinde olusturarak oyunu baslatiyorum. Kullaniciya devam edip etmeyecegini sorarak, islem yaptiriyorum.

def main():
    print("""
         -------- Taş-Kagit-Makas oyununa hoş geldiniz! --------
          """)
    while True:
        oyuncusecim = oyuncu()
        bilgisayarsecim = bilgisayar()  
        print(f"Siz: {oyuncusecim} Bilgisayar: {bilgisayarsecim}")  
        print(sonuc(oyuncusecim, bilgisayarsecim))  
        devam = input("Tekrar oynamak icin 'e'ye, cikmak için herhangi bir tusa basin: ")
        if devam.lower() != 'e':
            break


#Burada ise oyunu baslatiyorum. Oyunu fonksionlar icerisinde calistirdigim icin program hepsini gecerek, son satirda calistirmak istedigim fonksionu cagiriyor. Tabii bu ana fonksion oldugu icin oyun basliyor.
main()