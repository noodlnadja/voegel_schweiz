import requests as rq
import pandas as pd

url = "https://www.vogelwarte.ch/wp-content/assets/json/bird/list_de.json"
response = rq.get(url)

print(response)

data = response.json()
print(data)

data_df = pd.DataFrame(data)
print(data_df)
print(data_df.columns)
print(len(data_df.index))