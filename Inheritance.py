"""
12.04.2022

Inheritance Örnek:
"""


class Calisan:
    zam_orani = 1.1

    def __init__(self, isim, soyisim, yas):
        self.isim = isim
        self.soyisim = soyisim
        self.yas = yas
        self.email = isim + soyisim + "@gmail.com"

    def bilgileri_goster(self):
        return f"Ad:{self.isim}, Soyad:{self.soyisim}, Yas:{self.yas}, Email:{self.email}"


class Yazilimci(Calisan):
    zam_orani = 1.2

    def __init__(self, isim, soyisim, yas, telefon):
        super().__init__(isim, soyisim, yas)
        self.telefon = telefon

    def bilgileri_goster(self):
        return f"Ad:{self.isim}, Soyad:{self.soyisim}, Yas:{self.yas}, Email:{self.email}, Telefon{self.telefon}"


insan1 = Calisan("Mehmet","Kara", 35)

yazilimci1 = Yazilimci("Melike","Edgir",49, "Iphone")
yazilimci2 = Yazilimci("Pembe", "Soylu",22, "Xiaomi")

print(yazilimci2.bilgileri_goster())
print(yazilimci2.zam_orani)
print(insan1.zam_orani)
