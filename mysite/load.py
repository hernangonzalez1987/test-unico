from sqlalchemy import create_engine
import pandas
import os

DBHOST = os.getenv('DBHOST',default = "localhost")
DBPORT = os.getenv('DBPORT',default = "5432")
DBNAME = os.getenv('DBNAME',default = "unico")
DBUSER = os.getenv('DBUSER',default = "unico")
DBPASS = os.getenv('DBPASS',default = "unico")

engine = create_engine('postgresql://'+ DBUSER +':' + DBPASS + '@' + DBHOST +':' + DBPORT + '/' + DBNAME)

engine.execute('CREATE TABLE IF NOT EXISTS "markets_market" ("id" serial NOT NULL PRIMARY KEY, "longitude" double precision NULL, "latitude" double precision NULL, "setcens" double precision NULL, "areap" double precision NULL, "cod_dist" integer NULL, "district" text NULL, "cod_sub_prefecture" text NULL, "sub_prefecture" text NULL, "region_5" text NULL, "region_8" text NULL, "name" text NULL, "registry" text NULL, "address_street" text NULL, "address_number" text NULL, "address_city" text NULL, "reference" text NULL);')

market = pandas.read_csv('DEINFO_AB_FEIRASLIVRES_2014.csv')
market.columns = ['id', 'longitude', 'latitude','setcens','areap','cod_dist','district','cod_sub_prefecture','sub_prefecture','region_5','region_8','name','registry','address_street','address_number','address_city','reference']
market.to_sql('markets_market', engine, if_exists='append', index = False)