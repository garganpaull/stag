import time
import datetime
from datetime import date, datetime
import pandas as pd

'''tickers=[
'EUR.AX',
'SMI.AX',
'ASN.AX',
'LMG.AX',
'TNG.AX',
'CAE.AX',
'EQR.AX',
'LRS.AX',
'LIN.AX',
'SRN.AX',
'CXM.AX',
'MNB.AX',
'TMT.AX',
'AGY.AX',
'ARR.AX',
'WIN.AX',
'ATC.AX',
'AUC.AX',
'STM.AX',
'ZNC.AX',
'ARU.AX',
'RED.AX',
'TTM.AX',
'AR1.AX',
'RNU.AX',
'AJL.AX',
'QGL.AX',
'AGE.AX',
'CKA.AX',
'TIG.AX',
]
'''


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

    xlwriter=pd.ExcelWriter('Model(3DMACDverJul22)PU.xlsx', engine='openpyxl')

    for i in tickers:
        stock=YahooWebQuery=f"https://query1.finance.yahoo.com/v7/finance/download/{i}?period1={period1}&period2={period2}&interval=1d&events=history&includeAdjustedClose=True"
        df=pd.read_csv(stock)
        df = df.iloc[: , :-2]
        df.to_excel(xlwriter, sheet_name=i[0:3],startrow=7,startcol=2)
        print(df)

 

tickers=[
'SRN.AX'
]


ETL(tickers)