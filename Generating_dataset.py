import numpy as np
import pandas as pd
import os

# Read files
duration_data = pd.read_pickle('DataFrames/duration_data.dat')
fluence_data = pd.read_pickle('DataFrames/fluence_data.dat')

def cut_norm_lc(filename): #Prepare single light curve, cut to T100 and normalize by fluence
    grbname = filename[12:-7]
    #Cut lightcurve
    lc = pd.read_csv(filename, sep = ' ', header = None)
    lc = lc.loc[:, [0, 1, 3, 5, 7]]
    lc = lc.loc[lc.loc[:,0].apply(lambda x: duration_data.T100_start[grbname] <= x and x <= duration_data.T100_end[grbname])]
    lc.reset_index(drop=True,inplace=True)
    lc = lc.iloc[:,[1,2,3,4]] / float(fluence_data[grbname])
    return len(lc), lc
    


def prepare_lcs():
    # Go thorugh all LightCurves in the folder Light Curve and prepare them
    path = "LightCurves/"
 
    unpadded_curves = []
    grbnames = []
    errors = []
    # Go through alle the files
    max_len = 0 # Record longest burst
    for file in os.listdir(path):
        
        try: 
            grbnames.append(file[:-7])
            print(f"preparing {file}")
            length, lc = cut_norm_lc(path + file)
            if length <= 1:
                print(file)
                raise ValueError
            unpadded_curves.append(lc)
            if length > max_len:
                max_len = length
        except:
            errors.append(file)
            print(f"error with {file}")
        # os.remove(path + file)
    
    pd.to_pickle(unpadded_curves, "backup.dat")

    # Prepare empty dataset
    prepared_lcs = []

    # Go through and pad
    for lc in unpadded_curves:
        temp = np.zeros(shape = (max_len, 4))
        temp[:len(lc), :] = lc
        prepared_lcs.append(temp.reshape(-1))
        
    # Make to DataFrame
    prepared_dataset = pd.DataFrame(prepared_lcs)
    prepared_dataset.index = grbnames
    prepared_dataset.to_pickle('non_fft_dataset.dat')
    print(prepared_dataset)

if __name__ == "__main__":
    prepare_lcs()