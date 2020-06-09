# still has some work left
import pandas as pd
import numpy as np
T90 = pd.read_pickle('DataFrames/duration_data.dat')
T90 = T90['T90']

# df_short = pd.read_pickle('our_short_GRBs_with_time.dat') make this without time
df_short.columns = ['GRB name', 'T90']
df_short.set_index('GRB name', inplace=True, drop=True)
df_short['Cat'] = ['S' for _ in range(len(df_short.T90))]

# df_long = pd.read_pickle('our_long_GRBs_with_time.dat')
# df_long.columns = ['GRB name', 'T90']
# df_long.set_index('GRB name', inplace = True, drop = True)
# df_long['Cat'] = ['L' for _ in range(len(df_long.T100))]

# All_grbs = pd.read_pickle('all_GRBs_with_time.dat')
# All_grbs.columns= ['GRB name', 'T90']
# All_grbs.set_index('GRB name', inplace = True, drop = True)
# All_grbs['Cat'] = ['Discarded' for _ in range(len(All_grbs.T100))]

# All_grbs.loc[df_short.index, 'Cat'] = 'S'
# All_grbs.loc[df_long.index, 'Cat'] = 'L'
# All_grbs.T90 = All_grbs.T90.round(2)
# All_grbs.to_csv("Category_of_GRBs.csv")

# # All_grbs.Cat.describe(), All_grbs

# # data = pd.read_pickle('preFFT_dataset.dat')
# durationdata = pd.read_pickle("all_GRBs_with_T90_time.dat")
# durationdata.set_index("GRBname", inplace = True, drop = True)
# # durationdata

# ll_grbs.T100 = durationdata.loc[All_grbs.index]

# All = pd.concat([df_short, df_long])
# All = All.sort_values('GRB name')
# # All = All.set_index('GRB name', drop = True)
# # All = All.drop(['_'], axis = 1)
# All.T100 = All.T100.round(2)
