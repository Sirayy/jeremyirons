#%%
import pandas as pd

#%%
with open('res.txt') as f:
    period = f.read()
# %%
print(period)
# %%

#lista cykli
period_list=period.split("---------------\n")[:-1]
print(period_list)

period_list_dicto = []

for item in period_list:
    listed = item.split("\n")
    cycle= listed[0]
    first = listed[1].replace("Period start date: ", "")
    last =  listed[2].replace("Period end date: ", "")
    dicto = {"cycle":cycle, "start date":first, "end date":last}
    period_list_dicto.append(dicto)

#%%
print(period_list_dicto)

#%%
df_period=pd.DataFrame.from_dict(period_list_dicto)

df_period

#%%
for item in df_period:
    print(item)

#%%
#lista cykli
period_list2=period.split("---------------\n")
print(period_list2)

period_list_dicto2 = []

for index, item in enumerate(period_list2):
#enumerate dobre do debugowania
    print(index)
    listed2 = item.split("\n")
    cycle2= listed2[0]
    first2 = listed2[1].replace("Period start date: ", "")
    last2 =  listed2[2].replace("Period end date: ", "")
    dicto2 = {"cycle":cycle2, "start date":first2, "end date":last2}
    period_list_dicto2.append(dicto2)

period_list2[91]


#%%
with open('events.txt') as g:
    event = g.read()
# %%
print(event)
# %%

#lista eventów
event_list=event.split("\n")[:-1]
print(event_list)
#%%

event_list_dicto = []

for item in event_list:
    listed2 = item[:-3].split(" - ")
    print(listed2)
    id= listed2[0]
    date = listed2[1]
    event =  listed2[2]
    type = listed2[3]
    dicto2 = {"id":id, "date":date, "event":event, "type":type}
    event_list_dicto.append(dicto2)

#%%
print(event_list_dicto)

#%%
df_event=pd.DataFrame.from_dict(event_list_dicto)

df_event

elist = list(df_event["event"])

stats = {}

for event in elist:
    stats[event]=elist.count(event)

print(stats)

#%%
# select name, count(*) from elist
# group by name

df2 = df_event.groupby(['event'])['event'].count()
df2

#%%
df_event

for index, row in df_event.iterrows():
    print(row['event'])

#%%
#list unpacking
lista = ["czesc", "hi", "heloooo"]
v1, v2, v3 = lista 
print(v1, v2, v3)


#%%
moodies = {}
for index, row in df_event.iterrows():
    if row['event'] == 'Mood':
        if row['type'] in moodies:
            moodies[row['type']] += 1
        else:
            moodies[row['type']] = 1  

moodies = {'mood': moodies.keys(), 'fq': moodies.values()}

df_moodies=pd.DataFrame.from_dict(moodies)

print(df_moodies)
# %%
