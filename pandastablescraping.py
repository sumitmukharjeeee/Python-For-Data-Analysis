import pandas as pd
URL = 'https://en.wikipedia.org/wiki/List_of_highest-grossing_Indian_films/'
tables = pd.read_html(URL)
df = tables[0]
print(df)