import workbook
import xlwings as xw


excludeSheets=['0_SIGNALS','1_MODEL','4 EXCLUSIONS','UNIVERSE','3 SETTINGS']

def getTickers(file: str):

    tickers=[]
    with xw.App(visible=False) as app:
        wb = xw.Book(file) 
        
        for i in wb.sheets:
            tickers.append(i.name)
    tickers=[i for i in tickers if i not in (excludeSheets)]#remove sheets that are not model worksheets containing ticker data
    exchTickers=[]
    for i in tickers:
        exchTickers.append(f'{i}.AX')    


    #print(exchTickers)
    return (exchTickers)

#getTickers(workbook.getTestPriceUpdaterlFile())

        
            