# Author: <your name>
import argparse
# TODO: add additional imports

def convert_csv2sqlite(csv_name, sqlite_name, drop_last_n=0):
    #TODO: implement
    pass

parser = argparse.ArgumentParser(description='Converting covid19stats.alberta.ca csv file to custom sqlite db')
# TODO: add ArgumentParser arguments here


args = parser.parse_args()

convert_csv2sqlite(args.csv_filename, args.sqlite_filename, drop_last_n=args.drop)