import numpy as np
from astropy.utils.data import download_file
from spectral_cube import SpectralCube

filename_1 = download_file("https://almascience.eso.org/dataPortal/member.uid___A001_X1465_X3a33.BrickMaser_sci.spw71.cube.I.manual.image.pbcor.fits", cache=True)

filename_2 = download_file("https://almascience.eso.org/dataPortal/member.uid___A001_X87d_X141.a_sma1_sci.spw27.cube.I.pbcor.fits",cache=True)

cube1 = SpectralCube.read(filename_1)
cube1

cube2 = SpectralCube.read(filename_2)
cube2

cube1.find_lines(chemical_name=' H2CS ').show_in_notebook()
cube2.find_lines(chemical_name='SiO').show_in_notebook()