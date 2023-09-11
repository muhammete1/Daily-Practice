class Matbaa:
    murekkep = 100
    sarj = 100
    dergi = 0
    kontrol = 1
    sayac = 0
    dergi_olusturma_maliyeti = 0
    def __init__(self, dergi_ismi):
        self.ozel_karakter = "▮"
        self.dergi_ismi = dergi_ismi

    def Calis(self):
        if self.kontrol == 1:
            self.sayac += 1
            self.sarj -= 10
            self.murekkep -= 5
            self.dergi_olusturma_maliyeti += 1.5
            self.dergi_yuzde = (self.sayac / 20) * 100
            if self.sayac == 1:
                print("loading...")
            print("Dergi Oluşturuluyor:", "%", self.dergi_yuzde, self.ozel_karakter * self.sayac)
            if self.murekkep < 0 or self.sarj < 0:
                print("Şarjınız veya Mürekkebiniz Bitmiştir.Doldurmak için 1'e Çıkmak için 0'a Basın...")
                self.x = int(input())
                if self.x == 1:
                    if self.murekkep > self.sarj :
                        print("Şarjınız Bitmiş")
                        self.sarj = 100
                    elif self.sarj > self.murekkep:
                        print("Mürekkepiniz Bitmiş")
                        self.murekkep = 100
                    else :
                        print("Şarjınız Bitmiş")
                        print("Mürekkepiniz Bitmiş")
                        self.sarj =100
                        self.murekkep = 100
                elif self.x == 0:
                    print("Dergi Oluşturulamadı...")
                    quit()
            if self.sayac % 20 == 0:
                self.dergi += 1
                print(self.dergi,"Tane Dergi Oluşturuldu...")
                self.sayac = 0
    def BilgileriGoster(self):
        print("*"*30)
        print(self.dergi_ismi, "Adında Dergi Oluşturuldu.")
        print("Dergi Maliyeti:",self.dergi_olusturma_maliyeti)
        print("*" * 30)

def dergileriGoster(dergilerListesi):
    print("Tüm dergiler:")
    for i in dergilerListesi:
        print(i.dergi_ismi)

dergiler = []
flag = True
while flag == True:
    try:
        olusturma = int(input("Dergi oluşturmak istiyorsanız 1'e basın:"))
        if olusturma == 1:
            dergi_ismi = input("Derginin Adını Giriniz:")
            ayni_dergi_sayisi = int(input("Aynı Dergiden Ne Kadar Oluşturulsun:"))
            dergiler.append(Matbaa(dergi_ismi))
            for i in range(ayni_dergi_sayisi):
                for i in range(1,21):
                    dergiler[-1].Calis()
                dergiler[-1].BilgileriGoster()
                dergileriGoster(dergiler)
        else : flag = False
    except ValueError:
        print("Çıkış Yapılıyor...")
        quit()

#matbaa2 = Matbaa()

