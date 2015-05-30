# -*- conding: utf-8 -*-

import pandas as pd
import sys
from numpy import isnan
import pymongo

conn = pymongo.Connection()
db = conn['data-dev']

db.drop_collection('orgs')

df = pd.read_excel('/Users/Likit/Downloads/member-EQA-MUMT.xlsx',
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
