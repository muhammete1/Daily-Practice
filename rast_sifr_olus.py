import random
import time

liste = ["q","w","e","r","t","y","u","ı","o","p","ğ","ü","a","s","d","f","g","h","j","k","l",
         "ş","i","z","x","c","v","b","n","m","ö","ç",1,2,3,4,5,6,7,8,9,0]

b = random.randint(5,15)
print("Rastgele şifre oluşturuluyor...")
time.sleep(2)
for i in range(b):
    a = random.randint(0, 42)  # randint(0,32) metodu 0'ı ve 32'yi kapsar
    print(liste[a], end="")
#try:




