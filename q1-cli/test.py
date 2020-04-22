import pandas as pd
import sqlite3

# def count(n):

#     csv = pd.read_csv('covid19dataexport.csv')   # reading the file 
#     csv.rename(columns={"Date reported":"Date   Daily cases"}, inplace=True)
#     b = csv.pivot_table(index=['Date   Daily cases'], aggfunc='size')  # converts to number of casess pper day
    
#     drop = b[n]
#     print(drop)
csv = pd.read_csv('covid19dataexport.csv')   # reading the file 

b = csv['Date reported']


# c = csv[csv.duplicated(['Date reported'])]
# for i in c:
#     if c[i] in b:
#         count += 1
    
# print(c)
p = []
for i in b:
    if i not in p:
        p.append(i)
print(p)

c = []
for i in p:
     
# count(5)

# conn = sqlite3.connect('measurements2.db')
# cur = conn.cursor()

# cur.execute("SELECT * FROM alberta")
