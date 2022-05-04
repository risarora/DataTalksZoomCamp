import os
import pandas as pd
from sqlalchemy import create_engine
from time import time 
import sys
import argparse
import argparse



def main(params): 

  user = params.user
  password = params.password
  host = params.host
  port = params.port
  db_name = params.db_name
  table_name = params.table_name
  url = params.url
  

  csv_name = 'output.csv'
  
  os.system(f"wget {url} -O {csv_name}")

  engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db_name}')

  #day = sys.argv[1]
#  parser = argparse.ArgumentParser(description="Ingest CSV to postgres")
  df_iter = pd.read_csv(csv_name, iterator=True,chunksize=100000)
  

  #df = pd.read_csv('Downloads/zoom/100_yellow_tripdata_2021-01.csv')
  #print(pd.io.sql.get_schema(df,name='yellow_taxi_data',con=engine))

  df_iter
  while True :
      t_start = time()
      
      df=next(df_iter)
      df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
      df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)
      df.to_sql(name=table_name,con=engine,if_exists='append')
      df={''}
      t_endTime= time()
      print("inserted chunk ... took %.3f second"%(t_endTime - t_start))


if __name__ == '__main__':
  # user, password, host, post, db name, table name, csv path
  parser = argparse.ArgumentParser(description="Ingest CSV to postgres")

  parser.add_argument('--user', help='user for postgres')
  parser.add_argument('--password', help='password for postgres')
  parser.add_argument('--host', help='host for postgres')
  parser.add_argument('--port', help='post for postgres')
  parser.add_argument('--db_name', help='db name for postgres')
  parser.add_argument('--table_name', help='name of table in postgres')
  parser.add_argument('--url', help='url of the csv file to be loaded in postgres')

  args = parser.parse_args()
  main(args)


