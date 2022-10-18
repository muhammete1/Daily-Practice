import xlsxwriter

# Dosya oluşturma
planWorkbook = xlsxwriter.Workbook("notlar.xlsx")
planSheet = planWorkbook.add_worksheet("calculus")

harfler = ["A", "B", "C", "D"]
notlar = [10, 20, 50, 30]

# Blocklara yazı ekleme
planSheet.write("A1", "Harfler")
planSheet.write("B1", "Notlar")

for i in range(1, len(notlar)+1):
    planSheet.write(i,0, harfler[i-1])
    planSheet.write(i,1, notlar[i-1])

# planSheet.write(1,0, harfler[0])
# planSheet.write(0,1, notlar[0])

planWorkbook.close()
