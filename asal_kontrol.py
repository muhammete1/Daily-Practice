girdi = int(input("Bir asal sayı giriniz:"))
def asalKontrol(girdi):
    for i in range(2,girdi):
        if (girdi % i == 0):
            return ("Asal Sayıdır Değildir")
    return ("Asal Sayıdır")
print(asalKontrol(girdi))