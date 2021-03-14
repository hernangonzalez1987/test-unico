from sqlalchemy import create_engine
import pandas
import os
import sys

DBHOST = os.getenv('DBHOST',default = "localhost")
DBPORT = os.getenv('DBPORT',default = "5432")
DBNAME = os.getenv('DBNAME',default = "unico")
DBUSER = os.getenv('DBUSER',default = "unico")
DBPASS = os.getenv('DBPASS',default = "unico")

engine = create_engine('postgresql://'+ DBUSER +':' + DBPASS + '@' + DBHOST +':' + DBPORT + '/' + DBNAME)

result = engine.execute("SELECT EXISTS (SELECT * FROM information_schema.tables WHERE table_name = 'markets_market' );")
table_exists = result.first()[0]

if not table_exists:
    print( "Table Markets does not exist. Load should be run only after executing Markets App at least once")
    sys.exit(1)

market = pandas.read_csv('DEINFO_AB_FEIRASLIVRES_2014.csv')
market.columns = ['id', 'longitude', 'latitude','setcens','areap','cod_dist','district','cod_sub_prefecture','sub_prefecture','region_5','region_8','name','registry','address_street','address_number','address_city','reference']
market.to_sql('markets_market', engine, if_exists='append', index = False)