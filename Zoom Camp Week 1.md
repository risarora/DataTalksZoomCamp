# Zoom Camp Week 1

## Create Docker Images
```
PS C:\Users\Lenovo> wsl --list --verbose
  NAME                   STATE           VERSION
* Ubuntu                 Stopped         1
  docker-desktop-data    Running         2
  docker-desktop         Running         2
PS C:\Users\Lenovo> docker images
REPOSITORY               TAG       IMAGE ID       CREATED       SIZE
docker/getting-started   latest    cb90f98fd791   3 weeks ago   28.8MB

PS C:\Users\Lenovo>
PS C:\Users\Lenovo> docker run hello-world
Unable to find image 'hello-world:latest' locally
latest: Pulling from library/hello-world
2db29710123e: Pull complete                                                                                             Digest: sha256:10d7d58d5ebd2a652f4d93fdd86da8f265f5318c6a73cc5b6a9798ff6d2b2e67
Status: Downloaded newer image for hello-world:latest

Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (amd64)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
 https://hub.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/get-started/

PS C:\Users\Lenovo> docker run hello-world

Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (amd64)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
 https://hub.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/get-started/

PS C:\Users\Lenovo> docker run -it ubuntu bash
Unable to find image 'ubuntu:latest' locally
latest: Pulling from library/ubuntu
125a6e411906: Pull complete                                                                                             Digest: sha256:26c68657ccce2cb0a31b330cb0be2b5e108d467f641c62e13ab40cbec258c68d
Status: Downloaded newer image for ubuntu:latest
root@84565c57052c:/# ls
bin  boot  dev  etc  home  lib  lib32  lib64  libx32  media  mnt  opt  proc  root  run  sbin  srv  sys  tmp  usr  var
root@84565c57052c:/# pwd
/
root@84565c57052c:/# exit
exit
PS C:\Users\Lenovo> docker run -it python:3.8
Unable to find image 'python:3.8' locally 
3.8: Pulling from library/python
6aefca2dc61d: Pull complete
967757d56527: Pull complete
c357e2c68cb3: Pull complete
c766e27afb21: Pull complete
32a180f5cf85: Pull complete
1535e3c1181a: Pull complete
169cbf91df16: Pull complete
48c02d5c52ac: Pull complete
e1494a0c0d5d: Pull complete
sha256:f732d55571549b427e12edb89d0951372e7b73c67f717ad0645bb0cda19fc05e
Status: Downloaded newer image for python:3.8
Python 3.8.13 (default, Apr 20 2022, 18:53:37)
[GCC 10.2.1 20210110] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> exit
Use exit() or Ctrl-D (i.e. EOF) to exit
>>> exit()
PS C:\Users\Lenovo> 

PS C:\Users\Lenovo> docker run -it python:3.8 bash
root@4744a1d603b1:/# pip install pandas
Collecting pandas
  Downloading pandas-1.4.2-cp38-cp38-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (11.7 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 11.7/11.7 MB 5.3 MB/s eta 0:00:00
Collecting numpy>=1.18.5
  Downloading numpy-1.22.3-cp38-cp38-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (16.8 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 16.8/16.8 MB 7.3 MB/s eta 0:00:00
Collecting pytz>=2020.1
  Downloading pytz-2022.1-py2.py3-none-any.whl (503 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 503.5/503.5 KB 12.8 MB/s eta 0:00:00
Collecting python-dateutil>=2.8.1
  Downloading python_dateutil-2.8.2-py2.py3-none-any.whl (247 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 247.7/247.7 KB 12.8 MB/s eta 0:00:00
Collecting six>=1.5
  Downloading six-1.16.0-py2.py3-none-any.whl (11 kB)
Installing collected packages: pytz, six, numpy, python-dateutil, pandas
Successfully installed numpy-1.22.3 pandas-1.4.2 python-dateutil-2.8.2 pytz-2022.1 six-1.16.0
WARNING: Running pip as the 'root' user can result in broken permissions and conflicting behaviour with the system package manager. It is recommended to use a virtual environment instead: https://pip.pypa.io/warnings/venv
root@4744a1d603b1:/# python
Python 3.8.13 (default, Apr 20 2022, 18:53:37)
[GCC 10.2.1 20210110] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import pandas as pd
>>> exit()
root@4744a1d603b1:/# vi pipeline.py


PS C:\Users\Lenovo> docker run -it --entrypoint=bash python:3.9

```
## Python Docker Images

Docker file with pandas installed

* **Dockerfile_python_pandas.txt**

```
FROM python:3.9

RUN pip install pandas

ENTRYPOINT ["bash"]
```

```


```
docker build -t test:pandas
dockerfile.txt

```





Path
----
G:\Courses\Big Data and AWS\DE\Zoomcamp\week1


PS G:\Courses\Big Data and AWS\DE\Zoomcamp\week1> docker build -f Dockerfile.txt -t test:pandas .                       [+] Building 20.3s (6/6) FINISHED
 => [internal] load build definition from Dockerfile.txt                                                           0.0s
 => => transferring dockerfile: 107B                                                                               0.0s
 => [internal] load .dockerignore                                                                                  0.0s
 => => transferring context: 2B                                                                                    0.0s
 => [internal] load metadata for docker.io/library/python:3.9                                                      0.0s
 => [1/2] FROM docker.io/library/python:3.9                                                                        0.8s
 => [2/2] RUN pip install pandas                                                                                  17.7s
 => exporting to image                                                                                             1.7s
 => => exporting layers                                                                                            1.6s
 => => writing image sha256:6cb7ad456dc4ab34f08edfb5ae94a1083db0d2e8923f9edcd9a5ef26a7a7f354                       0.0s
 => => naming to docker.io/library/test:pandas                                                                     0.0s

Use 'docker scan' to run Snyk tests against images to find vulnerabilities and learn how to fix them
PS G:\Courses\Big Data and AWS\DE\Zoomcamp\week1>        

```



```
PS G:\Courses\Big Data and AWS\DE\Zoomcamp\week1> docker build -f Dockerfile.txt -t test:pandas .                       [+] Building 0.8s (9/9) FINISHED
 => [internal] load build definition from Dockerfile.txt                                                           0.0s
 => => transferring dockerfile: 155B                                                                               0.0s
 => [internal] load .dockerignore                                                                                  0.0s
 => => transferring context: 2B                                                                                    0.0s
 => [internal] load metadata for docker.io/library/python:3.9                                                      0.0s
 => [internal] load build context                                                                                  0.1s
 => => transferring context: 85B                                                                                   0.0s
 => [1/4] FROM docker.io/library/python:3.9                                                                        0.0s
 => CACHED [2/4] RUN pip install pandas                                                                            0.0s
 => [3/4] WORKDIR /app                                                                                             0.2s
 => [4/4] COPY pipeline.py pipeline.py                                                                             0.1s
 => exporting to image                                                                                             0.3s
 => => exporting layers                                                                                            0.2s
 => => writing image sha256:57cf934ff55a9360e97169c50a88310bc94276f0cbfd5cf2b34cac4e030bd275                       0.0s
 => => naming to docker.io/library/test:pandas                                                                     0.0s

Use 'docker scan' to run Snyk tests against images to find vulnerabilities and learn how to fix them 
```                                                                                                                                                                                                                                                                                                                                                                                                    

```

PS G:\Courses\Big Data and AWS\DE\Zoomcamp\week1\Docker_pythonPipeline> docker build -f Dockerfile.txt -t test:pandas .                                                                                                                         [+] Building 0.5s (9/9) FINISHED
 => [internal] load build definition from Dockerfile.txt                                                           0.0s
 => => transferring dockerfile: 173B                                                                               0.0s
 => [internal] load .dockerignore                                                                                  0.1s
 => => transferring context: 2B                                                                                    0.0s
 => [internal] load metadata for docker.io/library/python:3.9                                                      0.0s
 => [1/4] FROM docker.io/library/python:3.9                                                                        0.0s
 => [internal] load build context                                                                                  0.0s
 => => transferring context: 183B                                                                                  0.0s
 => CACHED [2/4] RUN pip install pandas                                                                            0.0s
 => CACHED [3/4] WORKDIR /app                                                                                      0.0s
 => [4/4] COPY pipeline.py pipeline.py                                                                             0.1s
 => exporting to image                                                                                             0.2s
 => => exporting layers                                                                                            0.1s
 => => writing image sha256:ba76778408c166e4d4f478a0999dee3cf785a5c88a07ddb9ae9da7a319c96010                       0.0s
 => => naming to docker.io/library/test:pandas                                                                     0.0s

Use 'docker scan' to run Snyk tests against images to find vulnerabilities and learn how to fix them
PS G:\Courses\Big Data and AWS\DE\Zoomcamp\week1\Docker_pythonPipeline> docker run -it test:pandas 2022-10-12           ['pipeline.py', '2022-10-12']
Hello Pipeline
 Job finishes on day =  {'2022-10-12'}
PS G:\Courses\Big Data and AWS\DE\Zoomcamp\week1\Docker_pythonPipeline> docker run -it test:pandas 2022-10-12 Hello User
['pipeline.py', '2022-10-12', 'Hello', 'User']
Hello Pipeline
 Job finishes on day =  {'2022-10-12'}
PS G:\Courses\Big Data and AWS\DE\Zoomcamp\week1\Docker_pythonPipeline>  

```



## Postgress Docker 
### DE Zoomcamp 1.2.2 - Ingesting NY Taxi Data to Postgres
* **https://www1.nyc.gov/site/tlc/about/tlc-trip-record-data.page**
```
services:
  pgdatabase:
    image: postgres:13
    environment:
      - POSTGRES_USER=root
      - POSTGRES_PASSWORD=root
      - POSTGRES_DB=ny_taxi
    volumes:
      - "./ny_taxi_postgres_data:/var/lib/postgresql/data:rw"
    ports:
      - "5432:5432"
  pgadmin:
    image: dpage/pgadmin4
    environment:
      - PGADMIN_DEFAULT_EMAIL=admin@admin.com
      - PGADMIN_DEFAULT_PASSWORD=root
    ports:
      - "8080:80"
    

```

#### Create postgresss docker image 
```

docker run -it \
      -e POSTGRES_USER="root" \
      -e POSTGRES_PASSWORD="root" \
      -e POSTGRES_DB="ny_taxi" \
      -v "G:/Courses/Big Data and AWS/DE/Zoomcamp/week1/2_Docker_postgresssDB/ny_taxi_postgres_data:/var/lib/postgresql/data" \
      -p "5432:5432" \
      postgres:13 

```

### Connect to postgress Server via CLI
* **install pgcli**
```
pip install pgcli

```

* **Login via pgcli**
```
PS C:\Users\Lenovo> pgcli -u root -d ny_taxi
Password for root:
Server: PostgreSQL 13.6 (Debian 13.6-1.pgdg110+1)
Version: 3.4.1
Home: http://pgcli.com
ny_taxi>
Time: 0.000s
ny_taxi> show tables;
unrecognized configuration parameter "tables"

Time: 0.004s
ny_taxi> exit
Goodbye!
PS C:\Users\Lenovo>                                                                                                                                      
```

## Install Jupyter

```
pip install jupyter

```

```
import pandas as pd
pd.__version__
```
'1.3.4'


```
```

```
from sqlalchemy import create_engine
df = pd.read_csv('Downloads/zoom/100_yellow_tripdata_2021-01.csv')
engine = create_engine('postgresql://root:root@localhost:5432/ny_taxi')
print(pd.io.sql.get_schema(df,name='yellow_taxi_data',con=engine))
```
```
CREATE TABLE yellow_taxi_data (
	"VendorID" BIGINT, 
	tpep_pickup_datetime TEXT, 
	tpep_dropoff_datetime TEXT, 
	passenger_count BIGINT, 
	trip_distance FLOAT(53), 
	"RatecodeID" BIGINT, 
	store_and_fwd_flag TEXT, 
	"PULocationID" BIGINT, 
	"DOLocationID" BIGINT, 
	payment_type BIGINT, 
	fare_amount FLOAT(53), 
	extra FLOAT(53), 
	mta_tax FLOAT(53), 
	tip_amount FLOAT(53), 
	tolls_amount FLOAT(53), 
	improvement_surcharge FLOAT(53), 
	total_amount FLOAT(53), 
	congestion_surcharge FLOAT(53)
)
```

```
df_iter = pd.read_csv('G:/Courses/Big Data and AWS/DE/Zoomcamp/Data/yellow_tripdata_2021-01.csv', iterator=True,chunksize=100000)
df_iter
while True :
    t_start = time()
    
    df=next(df_iter)
    df.tpep_pickup_datetime = pd.to_datetime(df.tpep_pickup_datetime)
    df.tpep_dropoff_datetime = pd.to_datetime(df.tpep_dropoff_datetime)
    df.to_sql(name='yellow_taxi',con=engine,if_exists='append')
    df={''}
    t_endTime= time()
    print("inserted chunk ... took %.3f second"%(t_endTime - t_start))

query=""" select count(*) from yellow_taxi"""
pd.read_sql(query,con=engine)

```

Col |count
---|---   
0 | 1369765



index | VendorID | tpep_pickup_datetime | tpep_dropoff_datetime | passenger_count | trip_distance | RatecodeID | store_and_fwd_flag | PULocationID | DOLocationID | payment_type | fare_amount | extra | mta_tax | tip_amount | tolls_amount | improvement_surcharge | total_amount | congestion_surcharge
---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---
0 | 18000 | 2 | 2021-01-01 18:48:52 | 2021-01-01 19:00:45 | 2 | 2.13 | 1 | N | 186 | 224 | 1 | 10.0 | 0.0 | 0.5 | 2.66 | 0.0 | 0.3 | 15.96 | 2.5   
0 | 18000 | 2 | 2021-01-01 18:48:52 | 2021-01-01 19:00:45 | 2 | 2.13 | 1 | N | 186 | 224 | 1 | 10.0 | 0.0 | 0.5 | 2.66 | 0.0 | 0.3 | 15.96 | 2.5
1 | 18001 | 2 | 2021-01-01 18:51:59 | 2021-01-01 19:02:08 | 1 | 5.62 | 1 | N | 132 | 130 | 2 | 17.0 | 0.0 | 0.5 | 0.00 | 0.0 | 0.3 | 17.80 | 0.0
2 | 18002 | 1 | 2021-01-01 18:11:44 | 2021-01-01 18:19:10 | 1 | 1.50 | 1 | N | 229 | 237 | 1 | 7.5 | 2.5 | 0.5 | 2.15 | 0.0 | 0.3 | 12.95 | 2.5
3 | 18003 | 1 | 2021-01-01 18:28:23 | 2021-01-01 18:35:23 | 2 | 1.40 | 1 | N | 263 | 239 | 1 | 7.0 | 2.5 | 0.5 | 2.05 | 0.0 | 0.3 | 12.35 | 2.5

0  18000  2  2021-01-01 18:48:52  2021-01-01 19:00:45  2  2.13  1  N  186  224  1  10.0  0.0  0.5  2.66  0.0  0.
/C:/Users/Lenovo/AppData/Roaming/jupyter/runtime/

/G:/Courses/Big Data and AWS/DE/Zoomcamp/Data

select max( tpep_pickup_datetime), min(tpep_dropoff_datetime),max(total_amount) from my_taxi

---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---
---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---
---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---


```
ny_taxi> select max( tpep_pickup_datetime), min(tpep_dropoff_datetime),max(total_amount) from yellow_taxi;
+---------------------+---------------------+---------+
| max                 | min                 | max     |
|---------------------+---------------------+---------|
| 2021-02-22 16:52:16 | 2008-12-31 23:07:22 | 7661.28 |
+---------------------+---------------------+---------+
SELECT 1
Time: 1.419s (1 second), executed in: 1.409s (1 second)
ny_taxi>

```


### Connect to postgress Server via pgadmin in Docker
#### Docker pull pgadmin image 
```
docker pull dpage/pdadmin4  
latest: Pulling from dpage/pgadmin4
40e059520d19: Pull complete
66f556fd213d: Pull complete
2a2fb8b45a9d: Pull complete
f4d0db21f3c0: Pull complete
cf30ad4c6765: Pull complete
be608843cead: Pull complete
49f606977dc4: Pull complete
1be4c4548360: Pull complete
6b9ca5a72134: Pull complete
08dbb28465b4: Pull complete
4350d02fd04a: Pull complete
1ee0bcd0d0ab: Pull complete
9135887d8024: Pull complete
6d23acfae6ef: Pull complete
Digest: sha256:f820e5579857a7210599f998c818777a2f6f39172b50fbeb2faaa1a70413e9ac
Status: Downloaded newer image for dpage/pgadmin4:latest

```
#### Docker run pgadmin 

```
docker run -it \
         -e PGADMIN_DEFAULT_EMAIL="root@root.com" \
         -e PGADMIN_DEFAULT_PASSWORD="root"  \
         -p "8080:8080" \
         dpage/pdadmin4

PS C:\Users\Lenovo> docker run -p 9000:80 -e 'PGADMIN_DEFAULT_EMAIL=test@gmail.com' -e 'PGADMIN_DEFAULT_PASSWORD=root' -d dpage/pgadmin4
3c58fbaf360f032c6f60b6485c145a02856a7cc508d01ba9d0d0257e4e0fca46
PS C:\Users\Lenovo> docker ps
CONTAINER ID   IMAGE            COMMAND                  CREATED              STATUS              PORTS                           NAMES
3c58fbaf360f   dpage/pgadmin4   "/entrypoint.sh"         About a minute ago   Up About a minute   443/tcp, 0.0.0.0:9000->80/tcp   kind_saha
10911d80f62e   postgres:13      "docker-entrypoint.s…"   2 minutes ago        Up 2 minutes        0.0.0.0:5432->5432/tcp          magical_black
cf19835081ba   python:3.9       "bash"                   31 hours ago         Up 31 hours                                         vigilant_booth
PS C:\Users\Lenovo> docker inspect 3c58fbaf360f032c6f60b6485c145a02856a7cc508d01ba9d0d0257e4e0fca46
```

### Connect to pgadmin
```
http://localhost:9000/login?next=%2F

```


### Create network to connect the two pgadmmin and pgdb
The pgamin image will not be able to connect to pgdatabase

```
docker network create pg-network 

docker run -it -e POSTGRES_USER="root" -e POSTGRES_PASSWORD="root" -e POSTGRES_DB="ny_taxi" -v "G:/Courses/DE/Zoomcamp/week1/2_Docker_postgresssDB/ny_taxi_postgres_data:/var/lib/postgresql/data" -p "5432:5432" --network pg-network --name pgdatabase postgres:13 

docker run -p 9000:80 -e 'PGADMIN_DEFAULT_EMAIL=test@gmail.com' -e 'PGADMIN_DEFAULT_PASSWORD=root' --network pg-network --name pgadminx dpage/pgadmin4

pgcli -u root -d ny_taxi

```

## 1.2.4 Dockerizing the Ingestion Script
### Converting the notebook to a Python script
```
jupyter nbconvert --to=script uploaddata.ipynb
```
### Using argparse

### Dropping table and Running the script
* **pipeline.py**
```
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
  parser.add_argument('--post', help='post for postgres')
  parser.add_argument('--db_name', help='db name for postgres')
  parser.add_argument('--table_name', help='name of table in postgres')
  parser.add_argument('--url', help='url of the csv file to be loaded in postgres')

  args = parser.parse_args()
  main(args)



```
### Run the python script 

```
docker run -it -e POSTGRES_USER="root" -e POSTGRES_PASSWORD="root" -e POSTGRES_DB="ny_taxi" -v "G:/Courses/DE/Zoomcamp/week1/2_Docker_postgresssDB/ny_taxi_postgres_data:/var/lib/postgresql/data" -p "5432:5432" --network pg-network --name pgdatabase postgres:13
```

```
pgcli -u root -d ny_taxi  

```

```
URL="https://nyc-tlc.s3.amazonaws.com/trip+data/yellow_tripdata_2022-01.csv"
python3 ingest_data.py  \
--user=root \
--password=root \
--host=localhost \
--port=5432 \
--db_name=ny_taxi \
--table_name=yellow_taxi \
--url=${URL}

```

```
PS C:\Users\Lenovo> docker run -it -e POSTGRES_USER="root" -e POSTGRES_PASSWORD="root" -e POSTGRES_DB="ny_taxi" -v "G:/Courses/DE/Zoomcamp/week1/2_Docker_postgresssDB/ny_taxi_postgres_data:/var/lib/postgresql/data" -p "5432:5432" --network pg-network --name pgdatabase postgres:13

PostgreSQL Database directory appears to contain a database; Skipping initialization

2022-05-04 20:35:30.935 UTC [1] LOG:  starting PostgreSQL 13.6 (Debian 13.6-1.pgdg110+1) on x86_64-pc-linux-gnu, compiled by gcc (Debian 10.2.1-6) 10.2.1 20210110, 64-bit
2022-05-04 20:35:30.938 UTC [1] LOG:  listening on IPv4 address "0.0.0.0", port 5432
2022-05-04 20:35:30.938 UTC [1] LOG:  listening on IPv6 address "::", port 5432
2022-05-04 20:35:30.981 UTC [1] LOG:  listening on Unix socket "/var/run/postgresql/.s.PGSQL.5432"
2022-05-04 20:35:31.047 UTC [27] LOG:  database system was shut down at 2022-05-04 20:09:25 UTC
2022-05-04 20:35:31.116 UTC [1] LOG:  database system is ready to accept connections
```


```
(zoom) root@Atishree:/mnt/g/Courses/DE/Zoomcamp/zoom# python3 ../week1/2_Docker_postgresssDB/ingest_data.py  --user=root --password=root --host=localhost --port=5432 --db_name=ny_taxi --table_name=yellow_taxi --url=${URL}
--2022-05-05 02:05:48--  https://nyc-tlc.s3.amazonaws.com/trip+data/yellow_tripdata_2022-01.csv
Resolving nyc-tlc.s3.amazonaws.com (nyc-tlc.s3.amazonaws.com)... 52.217.164.65
Connecting to nyc-tlc.s3.amazonaws.com (nyc-tlc.s3.amazonaws.com)|52.217.164.65|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 250275668 (239M) [text/csv]
Saving to: ‘output.csv’

output.csv                    100%[=================================================>] 238.68M  3.12MB/s    in 4m 57s

2022-05-05 02:10:46 (823 KB/s) - ‘output.csv’ saved [250275668/250275668]

inserted chunk ... took 14.562 second
inserted chunk ... took 14.765 second
inserted chunk ... took 15.307 second
inserted chunk ... took 14.667 second
inserted chunk ... took 13.236 second
inserted chunk ... took 15.975 second
inserted chunk ... took 13.506 second
inserted chunk ... took 11.255 second
inserted chunk ... took 11.284 second
inserted chunk ... took 11.647 second
inserted chunk ... took 17.313 second
inserted chunk ... took 11.910 second
inserted chunk ... took 11.981 second
inserted chunk ... took 11.504 second
inserted chunk ... took 14.432 second
inserted chunk ... took 13.494 second
inserted chunk ... took 11.989 second
inserted chunk ... took 11.510 second
inserted chunk ... took 20.493 second
inserted chunk ... took 14.021 second
inserted chunk ... took 13.742 second
inserted chunk ... took 15.578 second
inserted chunk ... took 13.792 second
inserted chunk ... took 7.641 second
StopIteration
```

### Dockerizing Ingestion Script
```
FROM python:3.9.1
RUN apt-get install wget
RUN pip install pandas sqlalchemy psycopg2
WORKDIR /app
COPY ingest_data.py ingest_data.py
ENTRYPOINT ["python","ingest_data.py"]

```

```
docker build -t taxi_ingest:v001 .

```
```
docker run -it -e POSTGRES_USER="root" -e POSTGRES_PASSWORD="root" -e POSTGRES_DB="ny_taxi" -v "G:/Courses/DE/Zoomcamp/week1/2_Docker_postgresssDB/ny_taxi_postgres_data:/var/lib/postgresql/data" -p "5432:5432" --network pg-network --name pgdatabase postgres:13
```

```
URL="https://nyc-tlc.s3.amazonaws.com/trip+data/yellow_tripdata_2022-01.csv"
docker run -it --network pg-network taxi_ingest:v001 --user=root --password=root --host=pgdatabase --port=5432 --db_name=ny_taxi --table_name=yellow_taxi --url="http://192.168.1.7:8000/Data/output.csv"



```


### HTTP server + ipconfig 
```
PS G:\Courses\DE\Zoomcamp\week1> python -m http.server
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
127.0.0.1 - - [05/May/2022 02:54:42] "GET / HTTP/1.1" 200 -
192.168.1.7 - - [05/May/2022 02:54:53] "GET / HTTP/1.1" 200 -
192.168.1.7 - - [05/May/2022 02:54:54] code 404, message File not found
192.168.1.7 - - [05/May/2022 02:54:56] "GET /Data/ HTTP/1.1" 200 -

```
* **Use ip/ifconfig to get the localhost ip and use it for fetching the file locally rather than from the web"**
  * replace URL="https://nyc-tlc.s3.amazonaws.com/trip+data/yellow_tripdata_2022-01.csv"
          with 
  * URL="http://192.168.1.7:8000/Data/output.csv"

### Troubleshooting the commands

* **host name docker run command**
* use --host=pgdatabase from from the docker run pgdatabase 

## Docker Compose to create yaml file for multiple images 

