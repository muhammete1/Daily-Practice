"""
Parantezlerin doğru açılıp kapandığını kontrol ediniz.

Input: s = "()[]{}"
Output: true
"""
s = "(([]){})"
#s = "()[])"

sözlük = {"(":")", "[":"]", "{":"}"}
dizi1 = list(sözlük.keys())
dizi2 = list(sözlük.values())
counter = 0
dogruluk_kon = 0
flag = 0
ilerle = 0

if (len(s) % 2 == 0):       # Burdaki amaç yan yana olan parantezlerin doğruluğunu kontrol etmek:
    for b in range(len(sözlük)):  # Burdaki amaç "s" yan yana açılan parantez mi baştan sondan açılan mı bunun konrolü
        if (s[0] == dizi1[b]):
            flag += 1
            if (s[1] == dizi2[b]):
                flag += 1

    if (len(s) == 2):       #Eğer s 2 karakterli ise bu işlemi yaptırıyoruz
        for y in range(len(sözlük)):
            if (s[0] == dizi1[y] and s[1] == dizi2[y]):
                dogruluk_kon += 1
    else :
        if (flag == 2):
            for i in range(len(s)-1):
                counter = 0
                for j in range(1, len(s), 2+ilerle):
                    if (counter == 0):
                        for k in range(len(sözlük)):  # 0 1 2
                            if (s[i] == dizi1[k] and s[j] == dizi2[k]):
                                dogruluk_kon += 1
                                counter += 1
        # sözlük = {"(": ")", "[": "]", "{": "}"}
        #s = "(([]){})"
        else:  #Burdaki amaç ise sondaki ve baştaki parantezin aynı olduğunu kontrol etmek:
            for z in range(int(len(s) / 2)):
                for q in range(len(sözlük)):
                    print(s[z] == dizi1[q] and s[-z-1] == dizi2[q])
                    if (s[z] == dizi1[q] and s[-z-1] == dizi2[q]):
                        dogruluk_kon += 1
    print("-----------")
    if ((len(s)/2) == dogruluk_kon):
        print(True)
    else : print(False)
else : print(False)





