#import universe
#run priceupdater to model worksheet
#if good, copy model to new worksheet
#save new spreadheet 
from csv import reader
import tickers, PriceUpdater
from workbook import getUniverseFile

#get list of tickers in our universe
def loaduniverse(file):
    with open(file) as read_obj:
        csv_reader=reader(read_obj)
        csv_data=list(csv_reader)
        tickers=[]
        for i in csv_data:
            tickers.append(i)
        return tickers


#enter tickers into model tosee which ones meet our KPI
def model():
    universe=getUniverseFile()
    tickers=loaduniverse(universe)
    
    for i in tickers:
        print (i[0])
    
model()


