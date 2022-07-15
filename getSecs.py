import time
import datetime
from datetime import date, datetime
import pandas as pd
import xlwings as xw



with xw.App(visible=False) as app:
    wb = xw.Book('MACD3D_mini.xlsx') 
    #wb = xw.Book(r'C:\Users\plemp\Dropbox\Stag Capital\Model(3DMACDverJul22)_PyVersion') 
    for i in wb.sheets:
        print(i)

        
        