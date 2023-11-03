#%%
import pandas as pd
import numpy as np
import traceback
import logging
#%%
for counter, value in enumerate(['v1', "v2", 'v3']): 
     print(counter)
# %%
for i in range(10):
     print(i)
# %%

for row in pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]]).iterrows():
    print(row)
    break
# %%
"czesc, co tam u cb, u mnie db".split(",")

# %%
",".join("czesc, co tam u cb, u mnie db".split(","))
# %%
def euro_palermo(suma: int):
		suma_euro=suma*4.53
		return(suma_euro)

euro_palermo(3000)
# %%
ojro=euro_palermo(3000)+1
ojro
# %%
print({"czesc":"cotam", "umnie":"spoko"}["ahaok"])
# %%
for i in list(range(0,11)):
      if i == 5:
            pass
      print(i)
# %%
lisztwa = [1, 19, 4, 7, 12, 3, 9, 10, 33, 34]
wartosc = lisztwa 
lisztwa2 = [i for i in lisztwa]
lisztwa3 = [i/2 for i in lisztwa]
lisztwa4 = [str(i) for i in lisztwa]
lisztwa5 = [[i, i+1, i+2] for i in lisztwa]
lisztwa6 = [i for i in lisztwa if i%2==0]
lisztwa7 = ['liczba '+ str(i) + ' to duza liczba :0' for i in lisztwa if i >= 10]
lisztwa8 = ['liczba '+ str(i) + ' to duza liczba :0' if i >= 10 else "liczba " + str(i) +" jest maciukipciu" for i in lisztwa ]
marcintupiel = tuple(i for i in lisztwa if i%2!=0)
dick = {"value_"+str(i):i for i in lisztwa}
print(lisztwa)
print(lisztwa2)
print(lisztwa3)
print(lisztwa4)
print(lisztwa5)
print(lisztwa6)
print(lisztwa7)
print(lisztwa8)
print(marcintupiel)
print(dick)
# %%
peppers = [2.5, 12.5, 5.5, 6.54, 8.3943094, 33.45734985485, 9]
peppers1 = [i**2 for i in peppers]
peppers2 = [i for i in peppers if i <=9]
peppers3 = ['z pepersz o dlugosci '+ str(i) + ' mozesz sie wspiac na górę' for i in peppers if i > 7]

print(peppers1)
print(peppers2)
print(peppers3)
# %%
wiek = 18
imie = 'roksi'

print('hej, czy wiesz ze ' + imie + ' ma juz ' + str(wiek) + ' lat')
print(f"hej, czy wiesz ze {imie} ma juz {str(wiek)} lat")
# %%
