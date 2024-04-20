import pandas as pd

df = pd.read_csv('ios-data.csv')

df = df.sort_values(by='Market Share', ascending=False)

labels = df['Version'].tolist()
values = df['Market Share'].tolist()

print(','.join(labels))
print(','.join(map(str, values)))