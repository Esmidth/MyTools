import xlrd,xlwt,sys,os;

Path=raw_input("File Path")
OriginalFile=raw_input("OriginalFile")
AimFile="F_"+OriginalFile

data=xlrd.open_workbook(Path+OriginalFile)
#data1=xlrd.open_workbook(Path+AimFile)

table=data.sheets()[0]
#table1=data1.sheets()[0]
wbk=xlwt.Workbook()
sheet=wbk.add_sheet('Sheet 1',cell_overwrite_ok=True)

#Copy data from the OriginalFile
col=0
row=0
while col < table.ncols:
	while row < table.nrows:
		if (table.cell(row,col).value.find("'")==-1):
			pass
		else:
			a=table.cell(row,col).value.find("'")
			Min=int(table.cell(row,col).value[0:a])
			Sec=int(table.cell(row,col).value[a+1:])
			Sec1=Min*60+Sec
			sheet.write(row,col,table.cell(row,col).value)
			sheet.write(row,col+2,Sec1)
		row = row +1
	col=col+1
	row=0
#Format the data From "min'sec" to sec
col=2
row=0

while row < table.nrows:
	sheet.write(row,col+2,int(sheet.cell(row,col+1).value)-int(sheet.cell(row,col).value))
	row = row+1
wbk.save(Path+AimFile)