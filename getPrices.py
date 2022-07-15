import time
import datetime
from datetime import date, datetime
import pandas as pd
import xlwings as xw



def ETL(tickers):

    data=pd.DataFrame()

   
    

    PrevYear=CurYear=date.today().year-1
    CurYear=date.today().year
    CurMth=date.today().month
    CurDate=date.today().day
    CurHour=datetime.now().hour
    CurMin=datetime.now().minute

    period1=int(time.mktime(datetime(PrevYear,CurMth,CurDate,CurHour,CurMin).timetuple()))
    period2=int(time.mktime(datetime(CurYear,CurMth,CurDate,CurHour,CurMin).timetuple()))

    with xw.App(visible=False) as app:
        
        wb = xw.Book('MACD3D_mini.xlsx') 
        #wb = xw.Book(r'C:\Users\plemp\Dropbox\Stag Capital\Model(3DMACDverJul22)_PyVersion') 
            
        
        for i in tickers:
            stock=YahooWebQuery=f"https://query1.finance.yahoo.com/v7/finance/download/{i}?period1={period1}&period2={period2}&interval=1d&events=history&includeAdjustedClose=True"
            df=pd.read_csv(stock)
            df = df.iloc[: , :-2]
            
            
            df.sort_values(by=['Date'])
            
            #load workbook
            sheet=i[0:3]
            ws = wb.sheets(sheet)

            #Update workbook at specified range
            ws.range('B7').options(index=False, header=False).value = df
            wb.save()



   

    #print(df)

    return ('PRICE UPDATE COMPLETE')

tickers=[
'SRN.AX','EUR.AX'
]


ETL(tickers)