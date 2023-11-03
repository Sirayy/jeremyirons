# %%
import pandas as pd
#%%
with open('events.txt') as f:
    events = f.read()
#%%
print(events)

#%%
events_list = events.split(sep='\n')[ : -1]
#%%
print(len(events_list))


#%%
events_dict = []
for poz in events_list:
    listed = poz.split(' - ')[ : -1]
    print(listed)
    event = listed[0]
    event_date = listed[1]
    event_type = listed[2]
    event_det = listed[3]

    dicto = {'event':event, "date":event_date, "type":event_type, 'details':event_det}

    events_dict.append(dicto)
#%%
print(len(events_dict))

# %%
events_df=pd.DataFrame.from_dict(events_dict)
#%%
print(events_df)
# %%
events_df_count = events_df.groupby(['type'])['type'].count()
#%%
events_df_grouped=events_df.groupby(['type'])['type']
events_df_count2=events_df_grouped.count()
print(events_df_count2)
# %%
print(events_df_count)
# %%
events_df.loc[[2,3,26], ['type', 'details']]

# %%
for i in range(5):
    print(i)
# %%
print(range(5))
# %%
list(range(5))
# %%
#od 5 do 27 
events_df.loc[list(range(5,28)), ['type', 'details']]

# %%
zm = list(range(3,31))
events_df.loc[zm, ['type', 'details']]
# %%
for numer, dane in events_df.iterrows():
    print(dane['type'])

# %%
for col in events_df:
    if col == 'type':
        print(events_df[col])
# %%
