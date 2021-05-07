import pandas as pd
import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, inspect, join, outerjoin, MetaData, Table
from config import connect_string


# engine = create_engine(connect_string)
# results = engine.execute("select * from asylumseekers")
# for row in results:
#     print(row)
#     break
# #engine = create_engine(connect_string)
# print(engine.table_names())
# print('all done')

engine = create_engine(connect_string)
# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)
# View all of the classes that automap found
Base.classes.keys()
# Save references to each table
Asylumseekers = Base.classes.asylumseekers
Demographics = Base.classes.demographics
Timeseries = Base.classes.time_series
# Create our session (link) from Python to the DB
session = Session(engine)
results = session.query(Asylumseekers.host_country, Asylumseekers.origin, Asylumseekers.year,Asylumseekers.month,Asylumseekers.value).\
            all() 
asy_seek = []
for result in results:
    temp_dict = {}
    temp_dict["Host Country"] = result.host_country
    temp_dict["Origin"] = result.origin
    temp_dict["Year"]= result.year
    temp_dict["Month"] = result.month
    temp_dict["Value"] = result.value
    asy_seek.append(temp_dict)
print(asy_seek)