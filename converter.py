import pandas as pd
import datetime
import math

rating_file = "./data/Criticker Ratings Jan 17 2025.csv"
output_file = "./data/to_letterboxd.csv"

df = pd.read_csv(rating_file, sep=",", encoding="UTF-8")

# converts from 1-100 to 1-10
df["Score"] = df["Score"].apply(lambda x: max(1, math.ceil(x / 10)))

# Step added to remove extra spaces in column names
df.columns = list(map(lambda x: x.strip(), df.columns))

# Rearranging columns
df = df[["IMDB ID", "Film Name", "Year", "Score", "Date Rated", "Mini Review"]]

# Rename columns to match Letterboxd format
df.rename(
    columns={
        "IMDB ID": "imdbID",
        "Film Name": "Title",
        "Year": "Year",
        "Score": "Rating10",
        "Date Rated": "WatchedDate",
        "Mini Review": "Review",
    },
    inplace=True,
)

# Converting date format to YYYY-MM-DD
df["WatchedDate"] = df["WatchedDate"].apply(
    lambda x: datetime.datetime.strptime(x, "%Y-%m-%d %H:%M").strftime("%Y-%m-%d")
)

df.to_csv(output_file, index=False)

print(f"Output file created: {output_file}")
