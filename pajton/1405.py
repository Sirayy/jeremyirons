#%%
import pandas as pd

#%%
with open('res.txt') as f:
    period_raw=f.read()

print(period_raw)
# %%
period_list=period_raw.split("---------------\n")[:-1]
print(period_list)
# %%
period_dict = []

for item in period_list:
    period_list_split=item.split("\n")[:-2]
    cycle = period_list_split[0].replace("cycle ", "")
    start = period_list_split[1].replace("Period start date: ", "")
    end = period_list_split[2].replace("Period end date: ", "")
    dicto = {'cycle':cycle, 'start':start, 'end':end}
    period_dict.append(dicto)

# %%
print(period_dict)
# %%
periods_df=pd.DataFrame.from_dict(period_dict)
# %%
print(periods_df)
#%%
pgroup = periods_df.groupby(['start'])['start']
print(pgroup.count())
# %%
periods_df.loc[list(range(2,50))]
# %%
for numer, dane in periods_df.iterrows():
    print(dane['start'])

# %%
for col in periods_df:
    if col=="start":
        print(periods_df[col])
# %%
for nr, item in periods_df.iterrows():
    print(item['start'])

# %%
