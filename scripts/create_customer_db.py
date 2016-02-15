from datetime import datetime

from sqlalchemy import (MetaData, Table, Column, Integer, Numeric, String,
        DateTime, ForeignKey, create_engine)

metadata = MetaData()

health_region = Table('health_regions', metadata,
        Column('id', Integer(), primary_key=True)
    )

geo_region = Table('geo_regions', metadata,
        Column('id', Integer(), primary_key=True, autoincrement=True),
        Column('name', String(40), index=True, nullable=False)
    )

province = Table('provinces', metadata,
        Column('id', Integer(), primary_key=True, autoincrement=True),
        Column('name', String(50), nullable=False),
        Column('health_region_id', ForeignKey('health_regions.id')),
        Column('geo_region_id', ForeignKey('geo_regions.id'))
    )

engine = create_engine('sqlite:///database/customer.db')
metadata.create_all(engine)
