import time
import datetime
from datetime import date, datetime
import pandas as pd
import xlwings as xw
from typing import Optional



def updatePrices(tickers: list, file: str, modelUpdate:Optional[bool]=False):

    PrevYear=CurYear=date.today().year-1
    CurYear=date.today().year
    CurMth=date.today().month
    CurDate=date.today().day
    CurHour=datetime.now().hour
    CurMin=datetime.now().minute

    period1=int(time.mktime(datetime(PrevYear,CurMth,CurDate,CurHour,CurMin).timetuple()))
    period2=int(time.mktime(datetime(CurYear,CurMth,CurDate,CurHour,CurMin).timetuple()))

    with xw.App(visible=False) as app:
        #Load Excel Workbook
        wb = xw.Book(file)
        sheets=wb.sheets
        curr_sheets=[]
        for i in sheets:
            curr_sheets.append(i.name)
        
        #grab data from Yahoo Finance per ticker
        
        for i in tickers:
            if modelUpdate==True and i[0:3] in curr_sheets :
                continue
            else:
                try:
                    stock=YahooWebQuery=f"https://query1.finance.yahoo.com/v7/finance/download/{i}?period1={period1}&period2={period2}&interval=1d&events=history&includeAdjustedClose=True"
                    df=pd.read_csv(stock)
                    #print(df)
                    df = df.iloc[: , :-2]#remove last two columns of pricing data from YF
                    df.sort_values(by=['Date'])
                except:
                    print(f'Error sourcing prices for ticker {i}')

            #select MODEL worksheet if doing a Model Update. If doing a Price Udpate, then select the worksheet of the ticker being updated.
            #DO THIS IF MODEL UPDATE

            #Load ticker data into Model
            if modelUpdate==True:
                sheet='MODEL'
                ws = wb.sheets(sheet)    
                ws.range('B7').options(index=False, header=False).value = df
                winTotalCount=ws.range('D2').value
                lossTotalCount=ws.range('E2').value
                totalTrades=winTotalCount+lossTotalCount
                winTotalAmt=float(ws.range('D3').value)
                lossTotalAmt=float(ws.range('E3').value)
                Return=float(ws.range('G3').value)
                totalPnL=float(winTotalAmt+lossTotalAmt)
                #avgWinPerTrade=winTotalAmt/winTotalCount
                
                #Check if ticker satisifies model investment criteria
                if Return>0.3:
                    wb.sheets.add(i[0:3])
                    active_sheet= wb.sheets[i[0:3]]
                    ws.range('A1:AG668').copy(wb.sheets[i[0:3]].range('A1:AG668'))
                    active_sheet.autofit(axis="columns")
                   
                      #Need to enter ticker into Signal Worksheet
                    '''SRC:  https://www.excell-en.com/blog/2019/7/9/python-code-to-find-next-empty-row-in-excel'''
                    ws_signal = wb.sheets('SIGNALS')
                    CellID =ws_signal.range('A' + str(ws_signal.cells.last_cell.row)).end('up').row + 1
                    CellRef = 'A' + str(CellID)
                    ws_signal.range(CellRef).value=i[0:3]
                    

            
            #DO THIS IF PRICE UPDATE
            else:
                sheet=i[0:3]#remove .AX from ticker as that is the sheet name.
                ws = wb.sheets(sheet)
                #Update workbook at specified range
                ws.range('B7:F400').clear()#clear existing data so no old data remains after update as can happen
                ws.range('B7').options(index=False, header=False).value = df
                
                
               

                                     
            wb.save()
        
    return None

    

    

#updatePrices(tickers,file)