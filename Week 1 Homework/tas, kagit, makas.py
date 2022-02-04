import random


birinci_kullanici = input("Lütfen adınızı giriniz")

x=  []
y= []
i = 1
while i <=10:

    secenekler = ["tas", "kagıt", "makas"]
    tas = secenekler[0]
    kagıt = secenekler[1]
    makas = secenekler [2]
    secim_bir = input(" Lütfen istediğinizi yazın: tas? kagıt? makas?")
    secim_iki = random.choice(secenekler)
    if secim_bir == "kagıt" and secim_iki == tas:
        print.end(f"{birinci_kullanici} kazandı")
        x.append(1) 
        # bunu  x.append(f"{birinci_kullanici} kazandı") ve sonrasında 
        # en son print(f"{birinci_kullanici}'nın kazandıgı oyun sayısı", len(x)) , 
        # tazında da yaptım. Benzer sonuç çıktı ama böyle daha güzel durdugu için bu sekilde teslim ettim.
    elif secim_bir == "tas" and secim_iki == makas:
        print(f"{birinci_kullanici}  kazandı")
        x.append(1) 
    elif secim_bir == "makas" and secim_iki == kagıt:
        print(f"{birinci_kullanici}  kazandı")
        x.append(1) 
    elif secim_bir == "tas" and secim_iki == kagıt:
        print("Bilgisayar kazandı")
        y.append(1)
    elif secim_bir == "makas" and secim_iki == tas:
        print("Bilgisayar kazandı")
        y.append(1)
    elif secim_bir == "kagıt" and secim_iki == makas:
        print("Bilgisayar kazandı")
        y.append(1)
    elif secim_iki == kagıt and secim_bir== "kagıt":
        print("Berabere")
    elif secim_iki == makas and secim_bir == "makas":
        print("Berabere")
    elif secim_iki == tas and secim_bir == "tas":
        print("Berabere")
    else:
        print("Tekrar deneyiniz")
    i+=1
x = sum(x)
y = sum (y)
print(f"{birinci_kullanici}'nın kazandıgı oyun sayısı", x)
print("Bilgisyar'ın kazandıgı oyun sayisi",y)

if x > y :
    print (f"{birinci_kullanici}, kazandı.")
elif x < y:
    print("Bilgisayar kazandı.")
else:
    print("Kazanan olmamıstır.")