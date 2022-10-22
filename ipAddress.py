"""
12.12.2021

Input: address = "1.1.1.1"
Output: "1[.]1[.]1[.]1"
"""
ip = "1.1.1.2"
def IP(ip):
    return ip.replace(".","[.]")
print(IP(ip))