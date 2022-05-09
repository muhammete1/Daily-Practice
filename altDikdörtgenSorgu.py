"""
16.12.2021

Bir dikdörtgeni oluşturucudaki tamsayılar matrisi olarak alan ve iki yöntemi destekleyen sınıfı uygulayın: SubrectangleQueries
1. updateSubrectangle(int row1, int col1, int row2, int col2, int newValue)
Sol üst koordinatı ve sağ alt koordinatı olan alt köşedeki tüm değerleri güncelleştirin
2. getValue(int row, int col)
Dikdörtgenden koordinatın geçerli değerini verir.

Input
["SubrectangleQueries","getValue","updateSubrectangle","getValue","getValue","updateSubrectangle","getValue","getValue"]
[[[[1,2,1],[4,3,4],[3,2,1],[1,1,1]]],[0,2],[0,0,3,2,5],[0,2],[3,1],[3,0,3,2,10],[3,1],[0,2]]
Output
[null,1,null,5,5,null,10,5]         // Output, Input'taki liste değerlerinin yazdırılmış hali.
Explanation
SubrectangleQueries subrectangleQueries = new SubrectangleQueries([[1,2,1],[4,3,4],[3,2,1],[1,1,1]]);
// The initial rectangle (4x3) looks like:
// 1 2 1
// 4 3 4
// 3 2 1
// 1 1 1
subrectangleQueries.getValue(0, 2); // return 1             //  listedeki 0'a 2 konumundaki değeri return'licek.
subrectangleQueries.updateSubrectangle(0, 0, 3, 2, 5);      //  0'a 0'dan, 3'e 2'ye kadar 5 değerini yazıcak.
// After this update the rectangle looks like:
// 5 5 5
// 5 5 5
// 5 5 5
// 5 5 5
subrectangleQueries.getValue(0, 2); // return 5
subrectangleQueries.getValue(3, 1); // return 5
subrectangleQueries.updateSubrectangle(3, 0, 3, 2, 10);
// After this update the rectangle looks like:
// 5   5   5
// 5   5   5
// 5   5   5
// 10  10  10
subrectangleQueries.getValue(3, 1); // return 10
subrectangleQueries.getValue(0, 2); // return 5
"""

class SubrectangleQueries:
    def __init__(self, rectangle):
        pass
    def updateSubrectangle(self, row1, col1, row2, col2, newValue):
        for i in range(row2 - row1 + 1):
            for j in range(col2 - col1 + 1):
                rectangle[row1 + i][col1 + j] = newValue
        for i in range(len(rectangle)):
            for j in range(len(rectangle[i])):
                print(rectangle[i][j], end=" ")
            print("")
    def getValue(self, row, col):
        return rectangle[row][col]

rectangle = [[3,9,4],[5,6,10]]
sub = SubrectangleQueries(rectangle)
sub.updateSubrectangle(1, 1, 1, 1, 5)
print(sub.getValue(1,0))
print(sub.getValue(1,0))
sub.updateSubrectangle(0, 0, 1, 0, 6);
print(sub.getValue(1,0))
print(sub.getValue(0,1))