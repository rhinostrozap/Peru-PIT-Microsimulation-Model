# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 17:22:16 2023

@author: wb395723
"""

import pandas as pd
import numpy as np

data = pd.read_csv("sample_data14.csv")

data = data.fillna(0)

data.to_csv("sample_data_peru.csv")
