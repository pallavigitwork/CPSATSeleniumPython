import xlwt
 
#----------------------------------------------------------------------
def main():
    #""""""
    book = xlwt.Workbook()
    sheet1 = book.add_sheet("PySheet1")
 
    for r in range(5): #rows [0,1,2,3,4]
        row = sheet1.row(r)
        for c in range(5):  #cols [0,1,2,3,4]
            data=(r)*10
            row.write(c,data) #index is where we want to write in the row, and value is the data created
 
    book.save("D:\\Eclipse\\workspace\\SeleniumWithPython\\SeleniumWithPython\\datasets\\test.xls")
 
#----------------------------------------------------------------------
if __name__ == "__main__":
    main()