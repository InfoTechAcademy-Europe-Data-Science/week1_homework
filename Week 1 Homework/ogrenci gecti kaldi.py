print("Bu uygulama ile Beden kitle indexine ulasacagız.")
kilo = int(input("Lütfen Kilonuzu giriniz: "))
boy = float(input("Lütfen Boyunuzu giriniz: "))
hesap =  kilo / boy **2 
if hesap < 25 :
    print("Sonucunuz 'Normal'dir")
elif hesap > 25 and hesap < 30 :
    print ("Sonucunuz 'Fazla kilo'dur'")
elif hesap > 30 and hesap < 40 :
    print("Sonucunuz 'Obez'dir ")

else:
    print("Sonucunuz 'Asırı Sisman'dır.")

