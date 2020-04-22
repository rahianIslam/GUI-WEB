import pandas as pd
import sqlite3

def count(n):

    csv = pd.read_csv('covid19dataexport.csv')   # reading the file 
    b = csv.pivot_table(index=['Date reported'], aggfunc='size')  # converts to number of casess pper day
    b.columns = ['Date']
    drop = b[0:n]
    print(drop)

# b = csv['Date reported']


# c = csv[csv.duplicated(['Date reported'])]
# for i in c:
#     if c[i] in b:
#         count += 1
    
# print(c)
# print([0])
count(5)

conn = sqlite3.connect('measurements2.db')
cur = conn.cursor()

cur.execute("SELECT * FROM alberta")