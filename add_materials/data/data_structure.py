import pandas as pd


df = pd.read_excel(r"C:\Users\1\Downloads\Telegram Desktop\botting.xlsx")
#r"C:\Users\1\Downloads\Telegram Desktop\botting.xlsx"
def split_records(row): # функция для изменения структуры записей
    if isinstance(row, str):
        row = row.strip("{").strip("}")
        themes = row.split(',')
        return themes
    else:
        return float('NaN')

# преобразовываем структуры записей к нужному виду
df['category'] = df['category'].map(split_records)
df['subcategory'] = df['subcategory'].map(split_records)

df_groupby_category = df.explode('category')
df_groupby_category = df_groupby_category.explode('subcategory')
df_groupby_category['subcategory'] = df_groupby_category['subcategory'].str.strip() # убираем лишние пробелы слева и справа, если они есть

# группируем уникальные подкатегории с категориями
df_groupby_category = df_groupby_category.groupby('category', as_index=False).agg({'subcategory': 'unique'})

# создаем словарь, где ключи - это уникальные значения колонки "category", а значения по ключам - это списки уникальных значений из колонки "subcategory"
dict_category = dict(zip(df_groupby_category['category'], df_groupby_category['subcategory']))