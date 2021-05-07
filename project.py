# Dependencies
import pandas as pd
import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, inspect, join, outerjoin, MetaData, Table
from config import connect_string

class AsylumSeekers():
    def __init__(self):
    self.engine = create_engine(connect_string)
    # self.conn = self.engine.connect()
    self.connect_string = connect_string
    self.inspector = inspect(self.engine)
    self.tables = self.inspector.get_table_names()
    self.Base = automap_base()
    self.Base.prepare(self.engine, reflect=True)
    self.Asylumseekers=self.Base.classes['asylumseekers']
    self.Demographics=self.Base.classes['demographics']
    self.TimeSeries=self.Base.classes['time_series']
    
    
    def asy_seekers_info(self):
        session = Session(self.engine)
        results = session.query(self.Asylumseekers)
        df = pd.read_sql(results.statement, session.connection())
        session.close()  
        return list(df.)  

    def demographics(self):
        session = Session(self.engine)
        results = session.query(self.Demographics)
        df = pd.read_sql(results.statement, session.connection())
        session.close()  
        return list(df.)

    def time_series_info(self): 
        session = Session(self.engine)
        results = session.query(self.TimeSeries)
        df = pd.read_sql(results.statement, session.connection())
        session.close()  
        return list(df.)   

   
   