# %%
import pandas as pd
import traceback
import logging


#%%
def data_to_list(file_name: str):
  with open(file_name, encoding="utf8") as f:
    rawfile=f.read()
    file_list = rawfile.split(sep="\n")[1:-1]
    print(file_list)
    return file_list
#%%
def list_to_dict(file_list: list):
    file_dict = []
    for item in file_list:
        try:
                list_split=item.split(";")
                movie_title = list_split[0]
                release_date = list_split[1]
                duration_minutes = list_split[2]
                genre = list_split[3]
                director = list_split[4]
                cast = list_split[5]
                language = list_split[6]
                country_of_origin = list_split[7]
                rating = list_split[8]
                box_office_revenue = list_split[9]
                currency = list_split[10]

                dict = {'Movie title':movie_title,
                        'Release date':release_date,
                        'Duration':duration_minutes,
                        'Genre':genre,
                        "Director":director,
                        "Cast":cast,
                        "Language":language,
                        "Country":country_of_origin,
                        "Rating":rating,
                        "Box office":box_office_revenue,
                        "Currency":currency
                        }
                file_dict.append(dict)
        except IndexError as e:
                logging.error(e)
                logging.error(traceback.format_exc())
                logging.error(file_list.index(item))
        except KeyError as e:
                logging.error(e)
                logging.error("HOLA GOLA")
                logging.error(file_list.index(item))

    return file_dict
#%%            
def dict_to_df(file_dict: dict):
        file_df=pd.DataFrame.from_dict(file_dict)
        print(file_df)
        return file_df
#%%
def df_statistics(df: pd.DataFrame, category: str):
        group = df.groupby([category])[category].count()
        print(group)
        return group
#%%
group = df_statistics(file_df, "Country")
#%%
def show_column(column: str, df: pd.DataFrame):
     for col in df:
          if col==column:
                print(df[col])
#%%
def enum(file_list: list, val: int):
        for count, item in enumerate(file_list, val):
                print(count, item)

#%%
def toplist(df: pd.DataFrame, col: str, val: int, head_tail: bool):
        for i in df[col].items():
            df[col] = df[col].astype(float) 
        if head_tail:
                print(df.nlargest(val, [col]))
        elif not head_tail: 
                print(df.nsmallest(val, [col]))
# %%
file_list = data_to_list("czinema_data.csv")
# %%
file_dict = list_to_dict(file_list)
# %%
file_df = dict_to_df(file_dict)
# %%
df_statistics(file_df, "Country")
# %%
show_column("Country", file_df)
# %%
enum(file_list, 100)
# %%
toplist(file_df, "Box office", 5, "hi")
# %%

