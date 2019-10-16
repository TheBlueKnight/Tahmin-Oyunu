import time
import random


print("""
*******************************************

Sayı Tahmin Etme Oyunu


1 ile 100  Arasında Bir Sayı Tahmin Edin

*******************************************

""")
rastgele=random.randint(1,100)
hak =7
while True:
    tahmin=int(input("Tahmininiz:"))
    print("{} Tahmin Hakkınız Kaldı.".format(hak))
    
    if tahmin<rastgele:
        print("Bilgiler Sorgulanıyor...\n")
        time.sleep(1)
        print("Daha Büyük Bir Sayı Tahmin Edin...\n")
        hak-=1
        print("{} Tahmin Hakkınız Kaldı.\n".format(hak))
    elif(tahmin>rastgele):
        print("Bilgiler Sorgulanıyor...\n")
        time.sleep(1)
        print("Daha Küçük Bir Sayı Tahmin Edin...\n")
        hak-=1
        print("{} Tahmin Hakkınız Kaldı.".format(hak))

    else:
        print("Bilgiler Sorgulanıyor...\n")
        time.sleep(1)
        print("Tebrikler!!! Sayımız\n",rastgele)
        break
    if (hak==0):
        print("Tahmin Hakkınız Bitmiştir...\n")
        print("Sayımız",rastgele)
        break
        
