import os


def getModelFile():

    path = r"C:\Users\plemp\Dropbox\Stag Capital"
    #file="Model(3DMACDverJul22)_LIVE.xlsx"
    file="Model(3DMACDverJul22)_PyTemp.xlsx"
    
    # Join various path components
    
    return(os.path.join(path, file))



def getUniverseFile():

    path = r"C:\Users\plemp\Dropbox\Stag Capital"
    file="SecUniverse.csv"
    
    # Join various path components
    
    return(os.path.join(path, file))

