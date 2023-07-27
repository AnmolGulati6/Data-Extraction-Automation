import pandas as pd

# Extract table from websites
website = pd.read_html('https://en.wikipedia.org/wiki/List_of_The_Simpsons_episodes_(seasons_1%E2%80%9320)')
print(len(website))  # 23 tables
print(website[1])  # first table

# Extract CSV files from websites
# target website = https://www.football-data.co.uk/data.php

# reading 1 csv file from the website
df_premier23 = pd.read_csv('https://www.football-data.co.uk/mmz4281/2223/E0.csv')

# showing dataframe
print(df_premier23)

# rename columns
df_premier23.rename(columns={'FTHG': 'HomeGoals', 'FTAG': 'AwayGoals'}, inplace=True)

# showing updated dataframe
print('df_premier23')

# Extract tables from PDF's

tables = camelot.read_pdf('foo.pdf', pages='1')
print(tables)
tables.export('foo.csv', f='csv', compress=True)
tables[0].to_csv('foo.csv')