import json
import numpy as np
import csv
import pandas as pd
from csv import writer
from csv import reader


df1 = pd.read_json('ckan_metadata_dump_20220526.json', lines=True)
df1.head()

df2 = pd.read_csv('ckan_views_20220526.csv')
df2.head()

df3 = pd.merge(df1, df2, how='left', left_on='name', right_on='dataset name')
df3.head()

columns = ['dataset id', 'dataset name']
df3.drop(columns, inplace=True, axis=1)

# df3.rename(columns={'State_x': 'State', 'Agency_type_x': 'Agency_Type', 'Agency_name_x':'Agency_Name',
#                          'vRace': 'Race', 'vRel': 'Religion', 'vSexOr': 'SexOrient',
#                           }, inplace=True)
# df3.head()

df3.to_csv("json_merged.csv", sep=',', encoding='utf-8')
df3.to_json("json_merged.json")
