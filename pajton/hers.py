#%%
para = """On 27 March 2019, around 1 a.m., Fitzpatrick (age 24) and Laading (25) along with their tour manager, Trevor Engelbrektson (37) from Minneapolis, were killed in a head-on traffic collision and subsequent vehicle fire near Milepost 68 on Interstate 10, west of Tonopah, Arizona.[19][20][21][22] They were travelling from Phoenix, Arizona, where they had played at The Rebel Lounge[23] on 26 March, to perform a show on the following evening in Santa Ana, California, some 350 miles (560 km) away, as part of a 19-date second tour of North America.[7][21] The Arizona Department of Public Safety confirmed that Engelbrektson had been driving the band's Ford tour van at the time of the crash.[21][24] The driver of a Nissan pick-up truck, Francisco Rebollar, aged 64, from Murrieta, California, was also killed in the collision; a subsequent police investigation of the scene located a bottle of alcohol in the wreckage.[25][21] At the time of the crash, the Arizona Department of Public Safety was already responding to reports of the Nissan pick-up truck travelling at speed in the wrong direction going eastbound on the westbound carriageway"""
para = para.replace(".", "")\
    .replace(",", "")\
    .replace("[19][20][21][22]", "")\
    .replace("[7][21]", "")\
    .replace("[25][21]", "")\
    .replace(")", "")\
    .replace("(", "")\
    .lower()\
    .split(" ")
print(para)

indeksy = []

for index, item in enumerate(para): 
    if item[0].isnumeric():
        indeksy.append(index)

print(indeksy)

dziwne = []

for index,item in enumerate(para):
    if index+1 in indeksy:
        dziwne.append(item)

print(para[0:5])
print(dziwne)