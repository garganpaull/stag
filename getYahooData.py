import time
import datetime
from datetime import date, datetime
import pandas as pd

ticker='EUR.AX'    


def ETL(ticker):

    PrevYear=CurYear=date.today().year-1
    CurYear=date.today().year
    CurMth=date.today().month
    CurDate=date.today().day
    CurHour=datetime.now().hour
    CurMin=datetime.now().minute

    print (PrevYear)
    print (CurMth)
    print (CurMin)

    period1=int(time.mktime(datetime(PrevYear,CurMth,CurDate,CurHour,CurMin).timetuple()))
    period2=int(time.mktime(datetime(CurYear,CurMth,CurDate,CurHour,CurMin).timetuple()))

    print(period1)
    print(period2)

    YahooWebQuery=f"https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={period1}&period2={period2}&interval=1d&events=history&includeAdjustedClose=True"
       
    df=pd.read_csv(YahooWebQuery)
    df.to_excel()
    print(df)

ETL(ticker)