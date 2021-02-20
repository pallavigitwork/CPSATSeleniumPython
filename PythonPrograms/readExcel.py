import xlrd
 
#----------------------------------------------------------------------
def open_file(path):
    """
    Open and read an Excel file
    """
    book = xlrd.open_workbook(path)
 
    # print number of sheets
    print(book.nsheets)
 
    # print sheet names
    print(book.sheet_names())
 

    # get the first worksheet
    first_sheet = book.sheet_by_index(0)
    
    
    #read the excel file cell by cell.
    for i in range(5):
        for j in range(5):
            cell = first_sheet.cell(i,j)
            print(int(cell.value))
 
#----------------------------------------------------------------------
if __name__ == "__main__":
    path = "D:\\Eclipse\\workspace\\SeleniumWithPython\\SeleniumWithPython\\datasets\\test.xls"
    open_file(path)