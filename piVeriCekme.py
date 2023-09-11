"""
11.09.2022

        *
       * *

pi sayısının istenilen hane kadar yazılması
"""

import requests
from bs4 import BeautifulSoup


def Input():
    digit = int(input("Please enter the digit of Pi:"))
    return digit


def Pi_scraping(digit):
    url = requests.get("https://barisozcan.com/pi-sayisi-ilk-100000-basamak/")
    soup = BeautifulSoup(url.content, "html.parser")
    div = soup.find("div", {"class": "entry-content"}).find("p").text
    print("After the comma:", end="")
    for i in range(2, digit+2):
        print(div[i], end="")


digit = Input()
Pi_scraping(digit)
