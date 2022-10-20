"""
21.06.2022

Hesap Makinesi Yapımı

Burada önemli olan control kısmı
"""
######################
#                    #
#      English       #
#                    #
######################


def control():
    while True:
        try:
            number = int(input("Please Enter Your Number:"))
            return number
        except:
            pass


while True:
    num1 = control()
    process = input("Please Enter Your Process:")
    transactions = ["+", "-", "*", "/"]
    contour = 0

    for i in transactions:
        if process == i:
            contour += 1
            num2 = control()
            if process == "+":
                print(f"{num1} {process} {num2} = {num1 + num2}")
            elif process == "-":
                print(f"{num1} {process} {num2} = {num1 - num2}")
            elif process == "*":
                print(f"{num1} {process} {num2} = {num1 * num2}")
            elif process == "/":
                print(f"{num1} {process} {num2} = {num1 / num2}")
    if contour != 1:
        print("There is no such process!")

######################
#                    #
#      Turkish       #
#                    #
######################


def sayi_kontrol():
    while True:
        sayi = input("sayi giriniz: ")
        try:
            sayi = int(sayi)
            return sayi

        except:
            print("sayi lazim sayi")


while True:
    sayi1 = sayi_kontrol()
    islemler = ["+", "-", "*", "/"]
    islem = input("islem giriniz:")
    sayac = 0

    for i in islemler:
        if i == islem:
            sayac += 1
            sayi2 = sayi_kontrol()
            if islem == "+":
                print(sayi1, f"{islem}", sayi2, "=", sayi1 + sayi2)
            elif islem == "-":
                print(sayi1, f"{islem}", sayi2, "=", sayi1 - sayi2)
            elif islem == "*":
                print(sayi1, f"{islem}", sayi2, "=", sayi1 * sayi2)
            elif islem == "/":
                print(sayi1, f"{islem}", sayi2, "=", sayi1 / sayi2)
    if sayac != 1:
        print("böyle bir işlem yok")