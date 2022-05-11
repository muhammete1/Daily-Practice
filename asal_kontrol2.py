girdi = int(input("Bir asal sayı giriniz:"))
def asalKontrol(girdi):
    for i in range(2,girdi):
        if (girdi % i == 0):
            return False
    return True
print(asalKontrol(girdi))