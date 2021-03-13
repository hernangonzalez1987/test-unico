import sqlite3
import pandas

conn = sqlite3.connect('db.sqlite3')

conn.execute('CREATE TABLE IF NOT EXISTS "markets_market" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "longitude" real NULL, "latitude" real NULL, "setcens" real NULL, "areap" real NULL, "cod_dist" integer NULL, "district" text NULL, "cod_sub_prefecture" text NULL, "sub_prefecture" text NULL, "region_5" text NULL, "region_8" text NULL, "name" text NULL, "registry" text NULL, "address_street" text NULL, "address_number" text NULL, "address_city" text NULL, "reference" text NULL);')

market = pandas.read_csv('deinfoabfeiraslivres2014.csv')
market.columns = ['ID', 'longitude', 'latitude','setcens','areap','cod_dist','district','cod_sub_prefecture','sub_prefecture','region_5','region_8','name','registry','address_street','address_number','address_city','reference']
market.to_sql('markets_market', conn, if_exists='append', index = False)