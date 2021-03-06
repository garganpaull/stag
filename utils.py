import xlwings as xw
import tickers,workbook


def copyCols(tickers, file, cols):

    with xw.App(visible=False) as app:
        #Load Excel Workbook
        wb = xw.Book(file)
        
        try:
            for i in tickers:
                #copy cols from MODEL sheet and paste to each ticker sheet 
                active_sheet= wb.sheets['1_MODEL']
                active_sheet.range(cols).copy(wb.sheets[i[0:3]].range(cols))
                active_sheet.autofit(axis="columns")
                print(i[0:3])
        except:
            print(f'Error sourcing prices for ticker {i}')

        wb.save()
    return 'Process Finished'
        
file=workbook.getModelFile()
tickers=tickers.getTickers(file)
cols='W6:W668'



def tickerWorkSheets(tickers, file):
#cop cols from MODEL
#paste to all other ticker sheets

    with xw.App(visible=False) as app:
        #Load Excel Workbook
        wb = xw.Book(file)
        
        try:
            for i in tickers:
                #copy cols from MODEL sheet and paste to each ticker sheet 
                wb.sheets[i[0:3]].delete()
                print(i[0:3])
        except:
            print(f'Error sourcing prices for ticker {i}')

        wb.save()
    return 'Process Finished'
        
file=workbook.getModelFile()
tickers=tickers.getTickers(file)
cols='W6:W668'
copyCols(tickers,file, cols)    


'''FUNCTIONS'''
#copyCols(tickers,file, cols)    
tickerWorkSheets(tickers, file)