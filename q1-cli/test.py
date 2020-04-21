import pandas as pd


count = 0

csv = pd.read_csv('covid19dataexport.csv')

b = csv['Date reported']
c = csv[csv.duplicated(['Date reported'])]
for i in c:
    if c[i] in b:
        count += 1
    
print(count)