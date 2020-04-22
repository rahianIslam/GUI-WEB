# Author: Rahian Islam
import argparse
import pandas as pd
from sqlalchemy import create_engine
import sqlite3
# TODO: add additional imports

def convert_csv2sqlite(csv_name, sqlite_name, drop_last_n=0):
    csv = pd.read_csv(csv_name)
    daily_cases = csv.pivot_table(index=['Date reported'], aggfunc='size')
    data_till_drop = daily_cases[0:drop_last_n]
    # dates = csv['Date reported']
    print(sqlite_name)

    db_uri = 'sqlite:///measurements2.db'
    engine = create_engine(db_uri, echo=False)
    data_till_drop.to_sql(name=sqlite_name, con=engine, if_exists='replace')
    engine.execute("SELECT * FROM sqlite_name")
    engine.dispose()
    
    


    

parser = argparse.ArgumentParser(description='Converting covid19stats.alberta.ca csv file to custom sqlite db')
# TODO: add ArgumentParser arguments here
parser.add_argument('csv_filename',type = argparse.FileType('r'), help = 'The csv file that needs to be converted')
parser.add_argument('sqlite_filename', help = 'The sqlite file to which csv has to be converted')
parser.add_argument('-d','--drop', help = 'Specify how many rows to drop')


args = parser.parse_args()
dropn = int(args.drop)
convert_csv2sqlite(args.csv_filename, args.sqlite_filename, drop_last_n=dropn)


# taek into pandas data frame then covert