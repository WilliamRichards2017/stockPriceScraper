###
###  Python Web Scraper for stock prices
###  Created by Will Richards
###
import urllib.request
import re

stock_file = open("stocklist.txt")

stock_list2 = stock_file.read()

stock_list = stock_list2.split("\n")


i=0

while i<len(stock_list):
    url = "http://finance.yahoo.com/q?s=" + stock_list[i] + "&fr=uh3_finance_web&uhb=uhb2"
    html_file = urllib.request.urlopen(url)
    html_text = html_file.read()
    regex = '<span id=\"yfs_l84_[^.]*\">(.+?)</span>'
    pattern = re.compile(regex)
    price = re.findall(pattern,html_text.decode("latin1"))
    print ("the price of",stock_list[i], "is", price   )
    i+=1
