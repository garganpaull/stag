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
        
        #grab data from Yahoo Finance per ticker
        
        for i in tickers:
            stock=YahooWebQuery=f"https://query1.finance.yahoo.com/v7/finance/download/{i}?period1={period1}&period2={period2}&interval=1d&events=history&includeAdjustedClose=True"
            df=pd.read_csv(stock)
            #print(df)
            df = df.iloc[: , :-2]#remove last two columns of pricing data from YF
            df.sort_values(by=['Date'])
            
            #select MODEL worksheet if doing a Model Update. If doing a Price Udpate, then select the worksheet of the ticker being updated.
            #DO THIS IF MODEL UPDATE
            if modelUpdate==True:
                sheet='MODEL'
                ws = wb.sheets(sheet)    
                ws.range('B7').options(index=False, header=False).value = df
                winTotalCount=ws.range('D2').value
                lossTotalCount=ws.range('E2').value
                totalTrades=winTotalCount+lossTotalCount
                winTotalAmt=ws.range('D3').value
                lossTotalAmt=ws.range('E3').value
                totalPnL=winTotalAmt+lossTotalAmt
                avgWinPerTrade=winTotalAmt/winTotalCount

                #print(winTotal)
                
            
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