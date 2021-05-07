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
# results = session.query(Asylumseekers.host_country, Asylumseekers.origin, Asylumseekers.year,Asylumseekers.month,Asylumseekers.value).\
#             all() 
# asy_seek = []
# for result in results:
#     temp_dict = {}
#     temp_dict["Host Country"] = result.host_country
#     temp_dict["Origin"] = result.origin
#     temp_dict["Year"]= result.year
#     temp_dict["Month"] = result.month
#     temp_dict["Value"] = result.value
#     asy_seek.append(temp_dict)
# print(asy_seek)
##########################################################################################################
# results = session.query(Demographics.year,Demographics.host_country, Demographics.location_name,\
#         Demographics.female_0_4, Demographics.female_5_11, Demographics.female_5_17,\
#         Demographics.female_12_17,Demographics.female_18_59, Demographics.female_60plus, \
#         Demographics.f_unknown, Demographics.f_total, Demographics.male_0_4,\
#         Demographics.male_5_11, Demographics.male_5_17, Demographics.male_12_17, \
#         Demographics.male_18_59, Demographics.male_60plus, Demographics.m_unknown, Demographics.m_total).\
#         all()
# dem =[]
# for result in results:
#     temp_dem = {}
#     temp_dem["Year"]=result.year
#     temp_dem["Host Country"]=result.host_country
#     temp_dem["Location"]=result.location_name
#     temp_dem["Female 0-4"]=result.female_0_4
#     temp_dem["Female 5-11"]=result.female_5_11
#     temp_dem["Female 5-17"]=result.female_5_17
#     temp_dem["Female 12-17"]=result.female_12_17
#     temp_dem["Female 18-59"]=result.female_18_59
#     temp_dem["Female 60+"]=result.female_60plus
#     temp_dem["Female unknown"]=result.f_unknown
#     temp_dem["Female total"]=result.f_total
#     temp_dem["Male 0-4"]=result.male_0_4
#     temp_dem["Male 5-11"]=result.male_5_11
#     temp_dem["Male 5-17"]=result.male_5_17
#     temp_dem["Male 12-17"]=result.male_12_17
#     temp_dem["Male 18-59"]=result.male_18_59
#     temp_dem["Male 60plus"]=result.male_60plus
#     temp_dem["Male unknown"]=result.m_unknown
#     temp_dem["Male total"]=result.m_total
#     dem.append(temp_dem)  
# print(dem)
##########################################################################################################
results = session.query(Timeseries.year, Timeseries.host_country, Timeseries.origin,Timeseries.population_type,Timeseries.value).\
            all() 
time = []
for result in results:
    temp_dict = {}
    temp_dict["Year"]= result.year
    temp_dict["Host Country"] = result.host_country
    temp_dict["Origin"] = result.origin
    temp_dict["Population Type"] = result.population_type
    temp_dict["Value"] = result.value
    time.append(temp_dict)
print(time)