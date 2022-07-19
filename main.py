import tickers, workbook,PriceUpdater, updateModel

'''PRODUCTION METHODS'''
def RunPriceUpdate():

    
    file=workbook.getModelFile()
    
    seclist=tickers.getTickers(file)
    PriceUpdater.updatePrices(seclist,file)
    print ('Price Update Complete')



def RunModelUpdate():

    universefile=workbook.getUniverseFile()
    modelfile=workbook.getModelFile()
    
    updateModel.model(universefile, modelfile)
    print ('Model Update Complete')

'''TEST METHODS'''
def RunPriceUpdateTEST():
    
    file=workbook.getTestPriceUpdaterlFile()
    
    seclist=tickers.getTickers(file)
    PriceUpdater.updatePrices(seclist,file)
    print ('Price Update Complete')



def RunModelUpdateTEST():
    universefile=workbook.getTestUniverseFile()
    modelfile=workbook.getTestModelFile()
    
    updateModel.model(universefile, modelfile)
    print ('Model Update Complete')

'''COMMAND'''

RunPriceUpdate()
#RunPriceUpdateTEST()

#RunModelUpdate()
#RunModelUpdateTEST()