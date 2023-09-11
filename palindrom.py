"""
Palindrome kelime ve sayı kontrol
"""
girdi = input("Bir kelime veya sayı giriniz:")


def PalindromeKontrol(girdi):
    i = 0
    sonuc = 0
    while (len(girdi) != i):
        if (girdi[i] == girdi[-i - 1]):
            sonuc += 1
        else:
            print("Sayınız palindrom değildir")
            break
        i += 1

    if (sonuc == len(girdi)):
        print("Kelime veya sayınız palindromdur.")


PalindromeKontrol(girdi)
