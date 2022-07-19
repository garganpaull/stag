import xlwings as xw
tickers=['foo','bar','poo']

for i in tickers:
    wb = xw.Book(r'C:\Users\plemp\Dropbox\Stag Capital\TEST FILES\WIN.xlsx')
    ws=wb.sheets('Sheet1')
    X =ws.range('A' + str(ws.cells.last_cell.row)).end('up').row + 1
    cell = 'A' + str(X)
    ws.range(cell).value=i
ws.autofit(axis="columns")
ws.SplitColumn = 1
ws.SplitRow = 1
ws.FreezePanes=True
    
#wb.save()