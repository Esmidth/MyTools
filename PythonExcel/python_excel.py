import xlwt, xlrd
import os

path = '/Users/esmidth/Desktop/excels/'
excels = sorted(os.listdir(path))
excels.pop(0)
print(excels)

wbk = xlwt.Workbook()
sheet = wbk.add_sheet('Sheet 1')
data1 = []
data2 = []
data3 = []

for x in range(29):
    data1.append(0)
for x in range(28):
    data2.append(0)
for x in range(25):
    data3.append(0)

for i, excel in enumerate(excels):
    data = xlrd.open_workbook(path + excels[i])
    tables = [data.sheets()[0], data.sheets()[1], data.sheets()[2]]
    for i, row in enumerate(range(tables[0].nrows - 1)):
        data1[i] += tables[0].cell(row + 1, 2).value
    for i, row in enumerate(range(tables[1].nrows - 1)):
        data2[i] += tables[1].cell(row + 1, 2).value
    for i, row in enumerate(range(tables[2].nrows - 1)):
        data3[i] += tables[2].cell(row + 1, 2).value
ii = 0
coll = 0

for i, data in enumerate(data1):
    data1[i] = data / 10;
    sheet.write(ii, coll, data1[i])
    ii += 1
for i, data in enumerate(data2):
    data2[i] = data / 10;
    sheet.write(ii, coll, data2[i])
    ii += 1
for i, data in enumerate(data3):
    data3[i] = data / 10;
    sheet.write(ii, coll, data3[i])
    ii += 1
print(data1, len(data1))
print(data2, len(data2))
print(data3, len(data3))
wbk.save(path + 'tst.xls')
