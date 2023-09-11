"""
01.01.2023

Bir n tamsayısı, 2 ile n - 2 (dahil) arasındaki her b tabanı için b tabanındaki n tamsayısının dize gösterimi
palindromik ise, kesinlikle palindromiktir.
Bir n tamsayısı verildiğinde, n kesinlikle palindromik ise true, aksi halde false döndürür.
Bir dize, ileri ve geri aynı şekilde okunuyorsa palindromiktir.

Input: n = 9
Output: yanlış
Explanation: 2 tabanında: 9 = 1001 (2 tabanında), palindromiktir.
Taban 3'te: 9 = 100 (taban 3), bu palindromik değildir.
Bu nedenle, 9 kesinlikle palindromik değildir, bu nedenle yanlış döndürürüz.
4, 5, 6 ve 7 tabanlarında n = 9'un da palindromik olmadığına dikkat edin.
"""

class Solution:
    def isStrictlyPalindromic(self, n: int):
        # n ifadesinin ikilik tabana dönüştürülmesi
        BINARY_BASE = ""
        # Matematikteki bölüm ifadesidir
        constValue = n

        for i in range(2, n-2):
            while n >= i:
                # remainder = kalan
                remainder = n % i
                BINARY_BASE += str(remainder)
                n = int(n / i)

            BINARY_BASE += str(n)
            n = constValue

            if BINARY_BASE != BINARY_BASE[::-1]:
                return False
            else:
                BINARY_BASE = ""


n = 9

sol = Solution()
print(sol.isStrictlyPalindromic(n))
