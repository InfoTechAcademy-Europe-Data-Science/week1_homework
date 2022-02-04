
import random
from re import X

birinci_kullanici = input("1. Kullancı: Lütfen adınızı giriniz")
ikinci_kullanici = input("2. Kullancı: Lütfen adınızı giriniz")

i = 1
while i <=10:
    secenekler = ["tas", "kagıt", "makas"]
    tas = secenekler[0]
    kagıt = secenekler[1]
    makas = secenekler [2]
    secim_bir = input("Birinci kullanici, Lütfen istediğinizi yazın: tas? kagıt? makas?")
    secim_iki = random.choice(secenekler)
    x = int()
    if secim_bir == "kagıt" and secim_iki == tas:
        print("Birinci kullancı kazandı")
        x +=1
    elif secim_bir == "tas" and secim_iki == makas:
        print("Birinci kullancı kazandı")
        x +=1
    elif secim_bir == "makas" and secim_iki == kagıt:
        print("Birinci kullancı kazandı")
        x +=1
    elif secim_bir == "tas" and secim_iki == kagıt:
        print("İkinci kullancı kazandı")
    elif secim_bir == "makas" and secim_iki == tas:
        print("İkici kullancı kazandı")
    elif secim_bir == "kagıt" and secim_iki == makas:
        print("İkinci kullancı kazandı")
    elif secim_iki == kagıt and secim_bir== "kagıt":
        print("Berabere")
    elif secim_iki == makas and secim_bir == "makas":
        print("Berabere")
    elif secim_iki == tas and secim_bir == "tas":
        print("Berabere")
    else:
        print("Tekrar deneyiniz")
    i+=1
print(x)