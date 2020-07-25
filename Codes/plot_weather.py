import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

df = pd.read_csv('1d_resolution.csv',parse_dates = [0])
weather = pd.read_csv('weather.csv',parse_dates = [0])

counts = df.groupby(df.tpep_pickup_datetime.dt.floor('1d')).sum()['counts']
counts = counts.reset_index()

plt.figure()
plt.scatter(counts.tpep_pickup_datetime, counts.counts, c = weather.Average, cmap='RdBu_r')
plt.colorbar(label='Average temperature')
plt.ylabel('Daily counts')
plt.xlabel('Date')
plt.xticks( rotation=25 )
plt.title('Daily taxi counts through out the year')
plt.savefig('counts_vs_dates.png',bbox_inches='tight', dpi=300)


