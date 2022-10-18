import xlrd

# Okunacak excel dosyasının adını yazıyoruz
dosya = "messages.xlsx"

# Okunacak dosya açılır
inputWorkbook = xlrd.open_workbook(dosya)

# Farklı excel sayfalarından çalışcağımız sheet açılır.(0) ilk sayfa
inputWorksheet = inputWorkbook.sheet_by_index(0)

print("Satır sayısı:",inputWorksheet.nrows)
print("Sütun sayısı:",inputWorksheet.ncols)

harfler = []
notlar = []
mesajlar = []

for i in range(1, inputWorksheet.nrows):
    harfler.append(inputWorksheet.cell_value(i, 0))
    notlar.append(inputWorksheet.cell_value(i, 1))
    mesajlar.append(inputWorksheet.cell_value(i,2))

print(harfler)
print(notlar)
print(mesajlar)
