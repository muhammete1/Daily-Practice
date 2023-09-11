"""
29.07.2022

    *
   * *

Merge Sort Algoritması : Diziyi her seferinde yarıya bölüyoruz. Sonr0asında bu bölünen parçaları sıralayarak tekrardan
bir bütün dizi haline getirmiş oluyoruz.
"""
# sirasiz_dizi = [10,87,2,-5,1,99,100]

def merge(dizi):
    if len(dizi) > 1:
        print("Parçalanan değerler", str(dizi))
        orta = len(dizi) // 2
        solDizi = dizi[:orta]
        sagDizi = dizi[orta:]

        merge(solDizi)
        merge(sagDizi)

        mergeSort(dizi, solDizi, sagDizi)


def mergeSort(dizi, solDizi, sagDizi):
    # Dizideki indisleri tutmamız için counter gereklidir.
    i = 0
    j = 0
    k = 0

    while i < len(solDizi) and j < len(sagDizi):
        if solDizi[i] < sagDizi[j]:
            dizi[k] = solDizi[i]
            i = i + 1
        else:
            dizi[k] = sagDizi[j]
            j = j + 1
        k = k + 1

    while i < len(solDizi):
        dizi[k] = solDizi[i]
        i = i + 1
        k = k + 1

    while j < len(sagDizi):
        dizi[k] = sagDizi[j]
        j = j + 1
        k = k + 1
    print("Birleştirilmiş hali...", str(dizi))


sirasiz_dizi = [10,87,2,-5,1,99,100]
merge(sirasiz_dizi)
