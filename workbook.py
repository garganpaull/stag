import os

'''PRODUCTION METHODS'''

prodpath=r"C:\Users\plemp\Dropbox\MACD3D"
testpath=r"C:\Users\plemp\Dropbox\MACD3D\TEST FILES"

def getModelFile():
    '''PRODUCTION FILES'''
    '''Both Price Updates and Model Updates will be made to this spreadsheet'''
    path = prodpath
    file="Model(3DMACDverJul22)_LIVE.xlsm"

    return(os.path.join(path, file))


def getUniverseFile():

    path = prodpath
    file="SecUniverse.csv"
    
    return(os.path.join(path, file))

'''TEST METHODS'''

def getTestPriceUpdaterlFile():
       
    '''TEST FILES'''
    path = testpath
    file="Model(3DMACDverJul22)_TEST_PRICEUPDATER.xlsx"
    
    return(os.path.join(path, file))
    
def getTestModelFile():
       
    '''TEST FILES'''
    path = testpath
    file="Model(3DMACDverJul22)_TEST_MODELUPDATE.xlsx"

    return(os.path.join(path, file))

def getTestUniverseFile():

    path = testpath
    file="SecUniverse_TEST_MODELUPDATE.csv"

    return(os.path.join(path, file))
