"""
Bir tamsayı verildiğinde, palindrome tamsayısı ise döndürün.
Input: x = 121
Output: true

Input: x = -121
Output: false
"""
number = int(input("Enter a number:"))

def isPalindrome(number):
    convert = str(number)
    counter = 0
    for i in range(1,len(convert)+1):
        if (convert[i-1] == convert[-i]):
            counter +=1
            if (counter == len(convert)//2):
                return True
        else : return False
    return False
print(isPalindrome(number))