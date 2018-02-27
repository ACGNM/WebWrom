import urllib2
import xlwt
from bs4 import BeautifulSoup

name_array = [];
book = xlwt.Workbook(encoding='utf-8',style_compression=0)
sheet = book.add_sheet('user_name',cell_overwrite_ok=True)

for num in range(10000,10020):

    request = urllib2.Request("https://gamewith.jp/user/profile/"+str(num))
    response = urllib2.urlopen(request)

    soup = BeautifulSoup(response)

    name = soup.select('div[class="_name fll"]')[0].get_text()

    name = name.strip()

    name_array.append(name)


print name_array[0]

for i, row in enumerate(name_array):
    sheet.write(i, 0, row)

book.save('/Users/gongzhihao/Desktop/names.xls')

