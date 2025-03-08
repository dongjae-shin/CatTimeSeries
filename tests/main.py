import os
import pandas as pd
import numpy as np
import CatNaviGATE.data.extract as ex

# Define the home directory and path to data
home_dir = os.path.expanduser("~")
path = (home_dir +
        "/Google Drive/Shared drives/Accelerating Innovations Team Drive/2. Research/8. Data/02 GC Experimental Data")
# Keywords to exclude
exclude_keywords = [
    "0p0005", # data with too low Rh mass, likely to be inaccurate
    "(1)",    # data mistakenly uploaded twice
    "PercentLoading_Synthesis_MassLoading_Temperature_Date_Location" # example Excel file
]

# Create an instance of DataForGP
dataset = ex.DataForGP(path=path)
# Find and filter Excel files
dataset.find_excel_files()
dataset.filter_excel_files(exclude_keywords=exclude_keywords, verbose=True)