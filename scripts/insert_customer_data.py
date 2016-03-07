# -*- coding: utf-8 -*-
import sys
import json
from sqlalchemy import create_engine, MetaData, Table

db = create_engine('sqlite:///'+sys.argv[1])
connect = db.connect()
meta = MetaData()


def add_data(table, attrs):
    ins = table.insert().values(**attrs)
    result = connect.execute(ins)
    return result.inserted_primary_key[0]


def insert_provinces(province_file=None, amphur_file=None):
    if not province_file or not amphur_file:
        raise IOError, "Province and amphur files are required."

    province_table = Table('provinces', meta, autoload=True, autoload_with=db)
    provinces = json.load(open(province_file))
    amphur_table = Table('amphurs', meta, autoload=True, autoload_with=db)
    amphurs = json.load(open(amphur_file))
    district_table = Table('districts', meta, autoload=True, autoload_with=db)
    for province in provinces:
        print(province)
        attrs = {'name': province}
        province_id = add_data(province_table, attrs)
        for amphur in provinces[province]:
            print('\t'+amphur)
            attrs = {'name': amphur,
                        'province_id': province_id,
                        'zip_code': '00000',
                        }
            amphur_id = add_data(amphur_table, attrs)
            for district in amphurs[amphur]:
                print('\t\t'+district)
                attrs = {'name': district, 'amphur_id': amphur_id}
                _ = add_data(district_table, attrs)


if __name__=='__main__':
    insert_provinces(sys.argv[2], sys.argv[3])
