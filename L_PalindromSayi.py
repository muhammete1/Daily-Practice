"""
Bir tamsayı verildiğinde, palindrome tamsayısı ise döndürün.
Input: x = 123
Output: 321
"""
x = int(input("Enter a Numbers:"))

def reverse(x):
    convert = str(x)
    if (x > 0):
        for i in range(1):
            if (-2**31<int(convert[::-1])<2**31):
                return int(convert[::-1])
            else : return 0
    else:
        convert = (str(-x))
        for i in range(1):
            y = int(convert[::-1])
            if (-2**31<-y<2**31):
                return -y
            else: return 0
print(reverse(x))