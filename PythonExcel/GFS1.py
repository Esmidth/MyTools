import xlrd
import xlwt

Path = raw_input("File Path\n")
OriginalFile = raw_input("OriginalFile\n")
AimFile = "F_" + OriginalFile

data = xlrd.open_workbook(Path + OriginalFile)
table = data.sheets()[0]
wbk = xlwt.Workbook()
sheet = wbk.add_sheet('Sheet 1', cell_overwrite_ok=True)

col = 0
row = 0
while row < table.nrows:
    if table.cell(row, col).value.find("'") == -1:
        pass
    else:
        # col0
        a = table.cell(row, col).value.find("'")
        Min0 = int(table.cell(row, col).value[0:a])
        Sec0 = int(table.cell(row, col).value[a + 1:])
        Sec01 = Min0 * 60 + Sec0
        # col1
        a = table.cell(row, col + 1).value.find("'")
        Min1 = int(table.cell(row, col + 1).value[0:a])
        Sec1 = int(table.cell(row, col + 1).value[a + 1:])
        Sec11 = Min1 * 60 + Sec1

        sheet.write(row, col, table.cell(row, col).value)
        sheet.write(row, col + 1, table.cell(row, col + 1).value)
        sheet.write(row, col + 2, Sec01)
        sheet.write(row, col + 3, Sec11)
        sheet.write(row, col + 4, Sec11 - Sec01)
    row += 1
wbk.save(Path + AimFile)
print "Done\n"