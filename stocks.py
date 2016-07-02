import urllib.request
import re

htmlfile = urllib.request.urlopen("http://finance.yahoo.com/q?s=aapl&fr=uh3_finance_web&uhb=uhb2")

htmltext = htmlfile.read()

regex = "<span id=\"yfs_l84_aapl\">(.+?)</span>"

pattern = re.compile(regex)

price = re.findall(pattern,htmltext.decode("latin1"))

print (price)
