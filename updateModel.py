#import universe (DONE)
#run priceupdater to model worksheet (DONE)
#if good, copy model to new worksheet
#save new spreadheet 
from csv import reader
import tickers, PriceUpdater
from workbook import getTestModelFile, getTestUniverseFile, getUniverseFile

#get list of tickers in our universe
def loaduniverse(file):
    with open(file) as read_obj:
        csv_reader=reader(read_obj)
        csv_data=list(csv_reader)
        tickers=[]
        for i in csv_data:
            tickers.append(i[0])
        return tickers


#enter tickers into model to see which ones meet our KPI
def model(universefile,modelfile):

    tickers=loaduniverse(universefile)

    PriceUpdater.updatePrices(tickers,modelfile, modelUpdate=True)

    return None




#model()



