import tickers, workbook,PriceUpdater

try:

    file=workbook.getModelFile()
    tickers=tickers.getTickers(file)
    PriceUpdater.updatePrices(tickers,file)
    print ('Price Update Complete')
except:
    print('An error occured')


