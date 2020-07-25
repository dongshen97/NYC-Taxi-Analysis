import pandas as pd

start_time = pd.to_datetime('2019-01-01 00:00:00')


months = ['01','02','03','04','05','06','07','08','09','10','11','12']
# we have to read all file at once, since some of records are in the wrong file

dfs = []

for month in months:
    df = pd.read_csv('yellow_tripdata_2019-{}.csv'.format(month), usecols=[1,3,4,7,8,13,16], parse_dates = [0])
    df = df[(df['tpep_pickup_datetime'] >= start_time) & (df['tpep_pickup_datetime'] < start_time + pd.DateOffset(months=1))]

    gb = df.groupby([df.tpep_pickup_datetime.dt.floor('1d'), df.PULocationID, df.DOLocationID])
    counts = gb.size().to_frame(name='counts')
    df = (counts
        .join(gb.agg({'passenger_count': 'mean'}).rename(columns={'passenger_count': 'passenger_count_mean'}))
        .join(gb.agg({'trip_distance': 'mean'}).rename(columns={'trip_distance': 'trip_distance_mean'}))
        .join(gb.agg({'tip_amount': 'mean'}).rename(columns={'tip_amount': 'tip_amount_mean'}))
        .join(gb.agg({'total_amount': 'mean'}).rename(columns={'total_amount': 'total_amount_mean'}))
        # .reset_index()
    )

    # dfs.append(df)
    df.to_csv('1d_resolution_{}.csv'.format(month))

    start_time = start_time + pd.DateOffset(months=1)




# dfs = pd.concat(dfs)
# dfs.to_csv('1d_resolution.csv')




