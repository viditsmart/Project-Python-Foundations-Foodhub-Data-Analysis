import pandas as pd

df = pd.read_csv('foodhub_order.csv')
pd.set_option('display.max_rows', None)
print(df)
