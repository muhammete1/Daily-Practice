"""
6.06.2022

@property decorator kullanımı

Bir class'ın fonksiyonunu, class'ın field'sı gibi gösterir.
"""


class Kisi:
    def __init__(self, ad, soyad):
        self.ad = ad
        self.soyad = soyad

    @property
    def email(self):
        return f"{self.ad}.{self.soyad}@gmail.com"

    def adSoyad(self):
        return f"{self.ad}.{self.soyad}"




kisi1 = Kisi("Mehmet", "Aksu")

print(kisi1.adSoyad())
print(kisi1.ad)
print(kisi1.email)
