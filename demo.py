import urllib2
import xlwt
import multiprocessing
from bs4 import BeautifulSoup

def process(num,start,end):
    name_array = [];

    book = xlwt.Workbook(encoding='utf-8', style_compression=0)
    sheet = book.add_sheet('user_name', cell_overwrite_ok=True)

    for num in range(start, end+1):
        request = urllib2.Request("https://gamewith.jp/user/profile/" + str(num))
        response = urllib2.urlopen(request)

        soup = BeautifulSoup(response)

        name = soup.select('div[class="_name fll"]')[0].get_text()

        name = name.strip()

        name_array.append(name)

    for i, row in enumerate(name_array):
        sheet.write(i, 0, row)


    book.save('/Users/gongzhihao/Desktop/names'+str(num) + '.xls')




if __name__ == '__main__':

    a = 10000
    b = 10499
    step = (b-a+1)/5

    for i in range(5):
        p = multiprocessing.Process(target=process, args=(i,a+i*step,a+(i+1)*step-1))
        p.start()

    print('CPU number:' + str(multiprocessing.cpu_count()))
    for p in multiprocessing.active_children():
        print('Child process name: ' + p.name + ' id: ' + str(p.pid))

    print('Process Ended')
