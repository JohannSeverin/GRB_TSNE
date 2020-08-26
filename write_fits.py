from astropy.io import fits
import pandas as pd

tab = pd.read_pickle('non_fft_dataset.dat')
hdu = fits.PrimaryHDU(tab)
hdul = fits.HDUList([hdu])
hdul.writeto('padded_lightcurves.fits')

tab.to_csv('padded_lightcurves.csv')
