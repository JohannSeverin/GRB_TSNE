import numpy as np
import pandas as pd
import os

# Read files
duration_data = pd.read_pickle('DataFrames/duration_data.dat')
fluence_data 

def prepare_lc(filename): #Prepare single light curve, cut to T100 and normalize by fluence
    grbname = filename[:,-7]
    #Cut lightcurve
    lc = pd.read_csv(grbname, sep = ' ', header = None)
    lc = lc.loc[:, [0, 1, 3, 5, 7]]
    lc = lc.loc[lc.loc[:,0].apply(lambda x: duration_data.T100_start[grbname] <= x and x <= duration_data.T100_end[grbname])]
    lc.reset_index(drop=True,inplace=True)
    #normalize lc
    lc = lc.iloc[:,[1,2,3,4]] / best_fit_fluence[grbname]
    





def cut_lcs():
    # Go thorugh all LightCurves in the folder Light Curve and prepare them
    path = "LightCurves/"
    
    # Make folder for prepared light curves if not existing
    if "prepared_curves" not in os.listdir():
        os.mkdir('prepared_curves')
    
    # Go through alle the files
    for file in os.listdir(path):
        prepare_lc(path + file)
        os.remove(path + file)



if __name__ == "__main__":
    cut_lcs