import xlrd
import csv

def csv_from_excel():
    wb = xlrd.open_workbook('ON AIR SITES DETAILS _180828.xlsx')


    # dynamically sheet name get

    # sheet_names = xl_workbook.sheet_names()
    # print('Sheet Names', sheet_names)   
    # sh = xl_workbook.sheet_by_name(sheet_names[0])

     # dynamically sheet name get ends

    sh = wb.sheet_by_name('DM sites')
    your_csv_file = open('your_csv_file.csv', 'wb')
    wr = csv.writer(your_csv_file, quoting=csv.QUOTE_ALL)

    for rownum in range(sh.nrows):
    	if sh.row_values(rownum) !='' and sh.row_values(rownum)!=" " and sh.row_values(rownum) !="\n":
	    	print(rownum)
	    	print(sh.row_values(rownum))
	        wr.writerow(sh.row_values(rownum))

    your_csv_file.close()

# runs the csv_from_excel function:
csv_from_excel()