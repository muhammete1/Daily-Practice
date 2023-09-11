import time

girdi = int(input("Para miktarınızı giriniz:"))

def Banka (girdi):
    girdi2 = int(input("Parayı bankaya yatırmak istiyorsanız 1'e çıkmak istiyorsanız 0'a basın:"))
    tire = "-"*20
    if(girdi2 == 1):
        for i in range(0,101):
            print("<", tire, "> yükleme tamamlanıyor", "%",i)
            if(i % 5 == 0):
                tire = tire.replace("-","*",1)
            time.sleep(0.1)
    else: return "Çıkış yapılıyor..."

Banka(girdi)