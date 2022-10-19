"""
22.05.2022

Fonksiyonlardan geri dönüş olarak fonksiyon return'licez
"""


def ChooseProcess(process):
    def addition(*args):
        return sum(args)

    def multi(*args):
        return int.__mul__(args)

    def medial(*args):
        return sum(args) / len(args)

    "--------- Burada fonksiyonu geri döndürüyoruz.Fonksiyon sonucu oluşan değeri değil. ---------"
    if process == "addition":
        return addition
    elif process == "multi":
        return multi
    else:
        return medial


a = ChooseProcess("addition")
print(a(2,3,4,5))
b = ChooseProcess("medial")
print(b(4,2,9))


def ChoosePerson(person):

    def chooseTeam(team):
        return f"{person} is to support {team}."
    return chooseTeam

c = ChoosePerson("Mehmet")
print(c("Galatasaray"))
d = ChoosePerson("Veli")
print(d("Beşiktaş"))
