"""
13.04.2022

Inheritance kendim yazıyorum
"""


class Calisan:
    def __init__(self, ad, soyad, yas):
        self.ad = ad
        self.soyad = soyad
        self.yas = yas

    def bilgileriGoster(self):
        return f"Ad:{self.ad}, Soyad:{self.soyad}, Yas:{self.yas}"

class Yazilimci(Calisan):
    def __init__(self, ad, soyad, yas):
        super().__init__(ad ,soyad,yas)
        self.email = self.ad + self.soyad + "@gmail.com"

    def bilgileriGoster(self):
        return f"Ad:{self.ad}, Soyad:{self.soyad}, Yas:{self.yas}, Email:{self.email}"

class Yonetici(Yazilimci):

    def __init__(self, ad, soyad, yas, maas):
        super().__init__(ad, soyad, yas)
        self.maas = maas
        self.calisanlar = []

    def calisanEkle(self,calisan):
        self.calisanlar.append(calisan)

    def calisanlariGoster(self):
        if not self.calisanlar:
            print("Çalışanınız Yok")
        else:
            for calisan_ in self.calisanlar:
                print(calisan_.bilgileriGoster())

calisan1 = Calisan("Mehmet","Durden", 79)

yazilimci1 = Yazilimci("Muhammet","Ebem", 22)
yazilimci2 = Yazilimci("Serkan","Tifer", 25)

yonetici1 = Yonetici("Sabri","Sarı", 57, 20000)
# yonetici1.calisanEkle(calisan1)
# yonetici1.calisanEkle(yazilimci2)
yonetici1.calisanlariGoster()