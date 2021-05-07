# Dependencies
import pandas as pd
import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, inspect, join, outerjoin, MetaData, Table, func
from config import connect_string

#################################################
# Database Setup
#################################################
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


class Asylum_Seekers():
    # def __init__(self):
    #     self.engine = create_engine(connect_string)
    #      # self.conn = self.engine.connect()
    #     self.connect_string = connect_string
    #     self.inspector = inspect(self.engine)
    #     self.tables = self.inspector.get_table_names()
    #     self.Base = automap_base()
    #     self.Base.prepare(self.engine, reflect=True)
    #     self.Asylumseekers=self.Base.classes['asylumseekers']
    #     self.Demographics=self.Base.classes['demographics']
    #     self.TimeSeries=self.Base.classes['time_series']
    
    
    def asy_seekers_info(self):
        
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
        return(asy_seek)    

    def demographics(self):
        session = Session(self.engine)
        results = session.query(self.Demographics)
        df = pd.read_sql(results, session.connection())
        session.close()  
        return list(df)

    def time_series_info(self): 
        session = Session(self.engine)
        results = session.query(self.TimeSeries)
        df = pd.read_sql(results, session.connection())
        session.close()  
        return list(df)   

   
   