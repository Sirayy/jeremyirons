#%%
import zipfile
import pandas as pd
import numpy as np
import traceback
import logging
import json
import random

#%%
zip_filepath="C:/Users/marys/OneDrive/Documents/GITHUB/jeremyirons/ZIPONATOR/raw data/ziponator_1.zip"

target_dir="C:/Users/marys/OneDrive/Documents/GITHUB/jeremyirons/ZIPONATOR/complete"

#%%
separator = {}
metadata_dic = {}
metadata_list = []
#%%
with zipfile.ZipFile(zip_filepath) as zf:
       for file in zf.namelist():
            if file.endswith(".csv"):
                zf.extract(file,target_dir)
                filename=file.replace(".csv", "")

            elif file.endswith("metadata"):
                    mt_file = open(file, 'r')
                    lines = mt_file.readlines()
                    print(lines)

                          


            

# %%
