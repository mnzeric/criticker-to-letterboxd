import pandas as pd
import datetime

df = pd.read_csv('ratings.csv',sep=',',encoding='UTF-8')

#Converting my rating format (0-10) for letterboxd rating10 converter, skip this to use rating (1-5)
df['Score'] = df['Score'].apply(lambda x: 1 if x == 0 else x)

#Step added to remove extra spaces in column names
df.columns = list(map(lambda x: x.strip(), df.columns))

#Rearranging columns
df = df[['IMDB ID', 'Film Name', 'Year', 'Score', 'Date Rated', 'Mini Review']]

df.rename(columns={'IMDB ID':'imdbID', 'Film Name':'Title', 'Year':'Year', 'Score':'Rating10', 'Date Rated':'WatchedDate', 'Mini Review':'Review'}, inplace=True)

#Converting date format
df['WatchedDate'] = df['WatchedDate'].apply(lambda x: datetime.datetime.strptime(x, '%b %d %Y, %H:%M').strftime("%Y-%m-%d"))

df.to_csv('to_letterboxd.csv', index=False)