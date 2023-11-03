#%%
import pandas as pd
import numpy as np
import traceback
import logging
#%%
dnd_list = ["name","url","cr","type","size","ac","hp","speed","align",
            "legendary","source","str","dex","con","int","wis","cha"]
#%%
print(dnd_list)
# %%
dnd_dict = {}
for item in dnd_list:
    dnd_dict[item]=None
    
# %%
dnd_dict
# %%
dnd_snip = ["abjurer","NULL","9","humanoid (any race)","Medium","12","84","NULL","any alignment","NULL","Volo's Guide to Monsters","NULL","NULL","NULL","NULL","NULL","NULL"]

#%%


#1. otworzyc plik i zwrocic liste rekordow
#2. lista -> slownik (parametry)

#%%
def data_to_list(file_name: str):
  with open(file_name, encoding='utf-8-sig') as f:
    rawfile=f.read()
    file_list = rawfile.split(sep="\n")
    print(file_list)
    return file_list

#%% 
def list_to_dict(file_name: str, sep: str):
        file_list = data_to_list(file_name)
        header = file_list[0].split(sep)
        dnd_dicts=[]

        for index, row in enumerate(file_list[1:]):
                dnd_dict = {}
                file_row_split=row.split(sep)
                
                for index2, item in enumerate(header):
                   # try:
                        dnd_dict[item]=file_row_split[index2]
                    # except IndexError as e:
                    #      print(file_row_split, index)
                    #      break
                dnd_dicts.append(dnd_dict)
        return dnd_dicts
#%%
def dict_to_df(file_dict: dict):
        file_df=pd.DataFrame.from_dict(file_dict)
        return file_df

#%%
dnd_monsters_dicts = list_to_dict("../raw_data/dnd_monsters.csv",",")

#%%
dnd_heroes_dicts = list_to_dict("../raw_data/heroes.csv",";")
dnd_heroes_dicts
#%%
dnd_links_dicts = list_to_dict("../raw_data/link_heroes_monsters.csv","|")
dnd_links_dicts

#%%
dnd_monsters_df = dict_to_df(dnd_monsters_dicts)
dnd_monsters_df['id']=np.arange(dnd_monsters_df.shape[0]).astype(int)
dnd_monsters_df['id']+=1
dnd_monsters_df

#%%
dnd_heroes_df = dict_to_df(dnd_heroes_dicts)
dnd_heroes_df['id']=dnd_heroes_df['id'].astype(int)
dnd_heroes_df

#%%
dnd_links_df = dict_to_df(dnd_links_dicts)
dnd_links_df['monster']=dnd_links_df['monster'].astype(int)
dnd_links_df['hero']=dnd_links_df['hero'].astype(int)
dnd_links_df

#%%
data_to_list("dnd_monsters.csv")

#%%
dnd_interactions = pd.merge(pd.merge(dnd_links_df,dnd_heroes_df,left_on='hero',right_on='id',how='left'), dnd_monsters_df, left_on='monster', right_on='id', how='left')
# dnd_interactions = pd.merge(dnd_heroes_links, dnd_monsters_df, left_on='monster', right_on='id', how='left')
dnd_interactions
# %%
for index, row in dnd_interactions.iterrows():
      print(row)
#%%
for index, row in dnd_links_df.iterrows():
      print(index)


#%%
for col in dnd_interactions:
      print(col)
#%%
for tup in dnd_heroes_df.iterrows():
     (index, row) = tup
     print(row)

#%%
listaaa = list(range(1,6))
print(listaaa)
v1, v2, v3, v4, v5=listaaa
print(v4)

#%%
dnd_interactions.columns
#%%
with open("../raw_data/dnd_interactions.csv", "w") as f #"a" - append 
    headers = list(dnd_interactions.columns)
    headers_join=";".join(headers)
    f.write(headers_join+'\n')
    for index, row in dnd_interactions.iterrows():
        values = list(row)
        values_join=";".join([str(i) for i in values])
        f.write(values_join+'\n')

#%%
with open("../raw_data/dnd_interactions.csv") as f:
    rawfile=f.readlines()
    for row in rawfile:
         print(row)
          


#%%
for index, row in dnd_interactions.iterrows():
      print(list(row))

#%%
dnd_heroes_df['id']
# %%

