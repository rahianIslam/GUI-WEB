# Author: Rahian Islam
import argparse
import pandas as pd
from sqlalchemy import create_engine
# TODO: add additional imports

def convert_csv2sqlite(csv_name, sqlite_name, drop_last_n=0):
    csv = pd.read_csv(csv_name)

    db_uri = 'sqlite:///measurements.db'
    engine = create_engine(db_uri, echo=False)
    csv.to_sql(name='sqlite_name', con=engine, if_exists='replace') 
    engine.dispose()
    print (csv)
    #TODO: implement

# def csv_read ():
#     # csv = pd.read_csv('csv_name')
#     print('abcd')
    

parser = argparse.ArgumentParser(description='Converting covid19stats.alberta.ca csv file to custom sqlite db')
# TODO: add ArgumentParser arguments here
parser.add_argument('csv_filename',type = argparse.FileType('r'), help = 'The csv file that needs to be converted')
parser.add_argument('sqlite_filename', help = 'The sqlite file to which csv has to be converted')
parser.add_argument('-d','--drop', help = 'Specify how many rows to drop')


args = parser.parse_args()

convert_csv2sqlite(args.csv_filename, args.sqlite_filename, drop_last_n=args.drop)


# taek into pandas data frame then covert