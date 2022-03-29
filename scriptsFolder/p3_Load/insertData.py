import pandas as pd 
import sqlalchemy
from sqlalchemy import create_engine
import uuid 
import requests


# after creating a account in hasura/supabase, get the credentials and insert them here 
# assuming postgres DB 

# load data to insert 
data = pd.read_csv('/Users/hantswilliams/Documents/development/python_projects/hospitalPriceline/cleanData/mountSinai_clean.csv')

####INITIAL FOR INSERTION OF UIDs
data['sbu_uuid'] = [uuid.uuid4() for _ in range(len(data.index))]


####HASURA or SUPABASE 

sqlUrl = sqlalchemy.engine.url.URL(
    drivername="postgresql+psycopg2",
    username='postgres',
    password='INSERTHERE',
    host='db.jhtjuigwarryaznleewj.supabase.co',
    port=6543,
    database='postgres',
)
engine = create_engine(sqlUrl)

# test engine
engine.connect()


# just keep first 5 rows for testing
data = data.head(5)

####INSERT DATA INTO HASURA/SUPABASE
data.to_sql('dataset_1', con=engine, if_exists='replace')