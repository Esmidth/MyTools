# -*- coding: utf-8 -*-
import xlrd
import xlwt

print "輸入目標路徑"
Path = raw_input()
print "輸入姓名列表文件"
NameList = raw_input()
print "輸入源文件"
OriginalFile = raw_input()
print "輸入需提取的分數文件"
SourceFile = raw_input()
print "第几次月考"
Times = input()
Path = "%s" % Path
Path += '\\'

data = xlrd.open_workbook(Path + NameList)
data1 = xlrd.open_workbook(Path + SourceFile)
data2 = xlrd.open_workbook(Path + OriginalFile)
table = data.sheets()[0]
table1 = data1.sheets()[0]
table2 = data2.sheets()[0]
wbk = xlwt.Workbook()
sheet = wbk.add_sheet('Sheet 1', cell_overwrite_ok=True)

t = 0
c = 0
while t < table2.nrows:
    while c < table2.ncols:
        sheet.write(t, c, table2.cell(t, c).value)
        c += 1
    t += 1
    c = 0
i = 0
a = 0
b = 0

while a < table.nrows:
    i = 0
    while i < table1.nrows:
        if table.cell(a, 0).value == table1.cell(i, 2).value:
            # print a,i
            c = 0
            while c < table1.ncols:
                sheet.write(5 * a + Times - 1, c + 1, table1.cell(i, c).value)
                c += 1
        i += 1
    a += 1
print "輸入目標文件名"
AimFileList = raw_input()
wbk.save(Path + AimFileList)
