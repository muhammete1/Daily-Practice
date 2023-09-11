"""
13.9.2022

pi sayısının siteden çekerek istenilen hane kadar yazdırılması

            *
           * *
"""

import requests
from bs4 import BeautifulSoup


def Input():
    digit = int(input("Please enter the digit of Pi:"))
    return digit


def Pi_scraping(digit):
    url = requests.get("http://3.141592653589793238462643383279502884197169399375105820974944592.com/index314159.html")
    soup = BeautifulSoup(url.content, "html.parser")
    div = soup.find("pre").text
    print(div[2])


digit = Input()
Pi_scraping(digit)
