import csv
from urllib.request import urlopen
from io import StringIO

data = urlopen('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data'
               '/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv').read().decode('ascii', 'ignore')
dataFile = StringIO(data)
csvReader = csv.reader(dataFile)
# 写文件打开
f = open('data/covid19_time_series.csv', 'w', encoding='utf-8')
csv_writer = csv.writer(f)
# 写入
for row in csvReader:
    csv_writer.writerow(row)
    print(row)
# 关闭
f.close()
