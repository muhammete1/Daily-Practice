"""
Bir dize dizisi arasında en uzun ortak önek dizesini bulmak için bir işlev yazın.
Ortak bir önek yoksa, boş bir dize döndürün.

Input: strs = ["flower","flow","flight"]
Output: "fl"
"""
strs = ["flower","flow","flight"]

def longestCommonPrefix(strs):
    list1 = []
    counter = 0
    counter2 = 0
    while (len(strs[0]) != counter):                    #7-16 arası ilk ve ikinci kelime arasında ortak arıyor
        while(len(strs[1]) != counter2):
            if (strs[0][counter] == strs[1][counter2]):
                list1.append(strs[0][counter])
                print("list1:" , list1)
                counter2 += 1
                break
            counter2 += 1
        counter +=1
        counter2 = 0
    for i in range(len(list1)-1):                       #17-21 ortak olan kelimelerden aynısı varsa listeden çıkarıyor
        for j in range(1,len(list1)-1):
            if(list1[i] == list1[j]):
                #list1.remove(list1[i])
                print("Yeni list1:" , list1)


    counter3 = 0
    list2 = []
    for i in range(len(list1)):                         #25-28 ortak olan kelimeler ile son kelimeyi karşılaştırıyor
        for j in strs[2]:
            if(list1[i] == j):
                list2.append(j)
                break

    print("list2:", list2)

    if (len(list2) > 2):                                #32-37 yine ortak kelimeleri listeden çıkarmaya yarıyor
        for i in range(len(list2) - 1):
            for j in range(1, len(list2) - 1):
                if (list2[i] == list2[j]):
                    list1.remove(list2[i])
                    print("Yeni list1:", list1)

    if (len(list2) > 0):                                #39-42 Liste dolu ise kelimeyi boş ise boş döndürüyor
        b = "".join(list2)
        return b
    else : return ""

print(longestCommonPrefix(strs))
