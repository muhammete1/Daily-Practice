"""
13.04.2022

Inheritance 2. Örnek Kullanımı
"""


class Calisan:

    def __init__(self, ad, soyad, maas):
        self.ad = ad
        self.soyad = soyad
        self.maas = maas

    def bilgileri_goster(self):
        return f"Ad:{self.ad} Soyad:{self.soyad} Maaş:{self.maas}"


class Yazilimci(Calisan):

    def __init__(self, ad, soyad, maas):
        super().__init__(ad, soyad, maas)
        self.email = self.ad + self.soyad + "@gmail.com"

    def bilgileri_goster(self):
        return f"Ad:{self.ad} Soyad:{self.soyad} Maaş:{self.maas} E-mail:{self.email}"


class Yonetici(Calisan):

    def __init__(self, ad, soyad, maas, calisanlar=[]):
        super().__init__(ad, soyad, maas)

        if calisanlar is None:
            pass
        else:
            self.calisanlar = calisanlar

    def calisan_ekle(self, calisan):
        if calisan not in self.calisanlar:
            self.calisanlar.append(calisan)

    def calisanlari_goster(self):
        for calisan in self.calisanlar:
            print(calisan.bilgileri_goster())


calisan1 = Calisan("Kemal", "Derviş", 5000)
calisan2 = Calisan("Sedat", "Kepir", 5200)

yazilimci1 = Yazilimci("Mustafa", "Turan", 8000)
yazilimci2 = Yazilimci("Aslı", "Tek", 8300)

yonetici = Yonetici("Mehmet", "Arat", 10000)
yonetici.calisan_ekle(calisan1)
yonetici.calisan_ekle(yazilimci2)
yonetici.calisan_ekle(yazilimci1)
yonetici.calisanlari_goster()

print(isinstance(yazilimci1, Yonetici))         # ->yazilimci1 Yonetici sınıfından türetilmemiştir
print(issubclass(Yonetici, Calisan))            # ->Yonetici sınıfı Calisan sınıfından türetilmiştir
