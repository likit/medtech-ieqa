# -*- conding: utf-8 -*-

import pandas as pd
import sys
from numpy import isnan
import pymongo
import os

conn = pymongo.Connection()
db = conn[os.getenv('MONGO_DBNAME')]

db.drop_collection('orgs')

df = pd.read_excel('member-EQA-MUMT.xlsx',
        2, parse_cols=[1,2,3], na_values='', header=None)

for row in df.iterrows():
    if not isnan(row[1][2]):
        org_dict = {
                'program': 'EQAC',
                'code': int(row[1][2]),
                'name': row[1][0],
                'labname': row[1][1],
                }
        db.orgs.insert(org_dict)
