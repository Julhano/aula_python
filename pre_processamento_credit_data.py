# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import pandas as pd

base = pd.read_csv('credit-data.csv')

base.describe()

base.loc[base['age'] < 0]

base.drop(base[base.age < 0].index, inplace=True)