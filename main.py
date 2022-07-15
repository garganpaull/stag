import tickers, workbook,PriceUpdater

try:

    file=workbook.getFile()
    tickers=tickers.getTickers(file)
    PriceUpdater.ETL(tickers,file)
    print ('Price Update Complete')
except:
    print('An error occured')


