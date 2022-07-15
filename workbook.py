import os


def getFile():

    path = r"C:\Users\plemp\Dropbox\Stag Capital"
    file="Model(3DMACDverJul22)_LIVE.xlsx"
    
    # Join various path components
    
    return(os.path.join(path, file))

