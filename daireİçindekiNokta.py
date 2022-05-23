"""
6.01.2022

Size 2D düzlemdeki noktanın koordinatlarının olduğu bir dizi verilir.
Birden çok nokta aynı koordinatlara sahip olabilir.points[i] = [xi, yi]

Ayrıca, queries'nin yarıçapıyla ortalanmış bir daireyi tanımlayan bir dizi de verilir. queries[j] = [xj, yj, rj]
Her sorgu için, daire içindeki nokta sayısını hesapla. Dairenin sınırındaki noktalar içindekabul edilir.
"""


class Solution:
    def countPoints(self):
        output = []
        counter = 0
        for i in range(len(queries)):
            for j in range(len(points)):
                distanceX = (points[j][0] - queries[i][0]) ** 2
                distanceY = (points[j][1] - queries[i][1]) ** 2
                distance = (distanceX + distanceY)**(1/2)

                if queries[i][-1] >= distance:
                    counter += 1
            output.append(counter)
            counter = 0

        return output


solution = Solution()

queries = [[2, 3, 1], [4, 3, 1], [1, 1, 2]]
points = [[1, 3], [3, 3], [5, 3], [2, 2]]

print(solution.countPoints())
