#%%
import pandas as pd

#%%
with open('eliot.txt') as eliottxt:
    eliot = eliottxt.read()

#read lines zwraca mi listę linijek w tekście, separatorem jest \n
#natomiast jesli calosc ma byc 1 stringiem to wtedy read

eliot=eliot.replace("\n", " ")\
    .replace(".", "")\
    .replace(",", "")\
    .replace("?", "")\
    .replace("’", "'")\
    .replace("                  ", "")\
    .replace("     ", " ")\
    .strip()\
    .lower()

eliot_list=eliot.split(" ")
print(eliot_list)

# %%
for word in eliot_list:
    print(word + ": " + str(len(word)))

#%% 
poem_info = {
    "author": "T.S. Eliot",
    "year": 1922,
    "pages": 62, 
    "name": "The Waste Land",
    "genre": "everything",
    "words": eliot_list
}

for cat in poem_info.values():
    print(cat)

#%%
for cat in poem_info:
    print(cat + ": " + str(poem_info[cat]))

#%%
var = "name"
print(poem_info[var])
#%%
empt = []

for word in eliot_list:
    empt.append(word[0])

stats = {}

for letter in empt:
    stats[letter]=empt.count(letter)

print(stats)
#%%
stats2 = {}

for letter in empt:
    if letter in stats2: 
        stats2[letter] += 1
    else:
        stats2[letter] = 1 
print(stats)
print(stats2)

stats2 = {'letter': stats2.keys(), 'fq': stats2.values()}

#%%
df_stats=pd.DataFrame.from_dict(stats2)
# %%
df_stats