"""
01.01.2023

Celcius'u Kelvin ve Fahrenheit derecelerine dönüştürme
"""

class Solution:
    def convertTemperature(self, celsius: float):
        if 0 <= celsius < 1000:
            Kelvin = celsius + 273.15
            Fahrenheit = celsius * 1.80 + 32.0
            ans = [Kelvin, Fahrenheit]
            return ans


celsius = 36.5

sol = Solution()
print(sol.convertTemperature(celsius))
