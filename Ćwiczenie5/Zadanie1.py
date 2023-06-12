import pickle
import pandas as pd
import pyarrow.parquet as pq
from openpyxl import Workbook

def generate_collection(size):
    return list(range(size))

def save_pickle(collection, filename):
    with open(filename, 'wb') as file:
        pickle.dump(collection, file)

def load_pickle(filename):
    with open(filename, 'rb') as file:
        return pickle.load(file)

def save_parquet(collection, filename):
    df = pd.DataFrame(collection)
    table = pa.Table.from_pandas(df)
    pq.write_table(table, filename)

def load_parquet(filename):
    table = pq.read_table(filename)
    df = table.to_pandas()
    return df[0].tolist()

def save_xlsx(collection, filename):
    wb = Workbook()
    sheet = wb.active

    for i, item in enumerate(collection):
        sheet.cell(row=i+1, column=1, value=item)

    wb.save(filename)

def load_xlsx(filename):
    wb = pd.read_excel(filename)
    return wb.iloc[:, 0].tolist()

collection_sizes = [100, 10000, 100000]
filename_base = 'collection'

for size in collection_sizes:
    collection = generate_collection(size)

    pickle_filename = f'{filename_base}_{size}_pickle.pickle'
    save_pickle(collection, pickle_filename)

    parquet_filename = f'{filename_base}_{size}_parquet.parquet'
    save_parquet(collection, parquet_filename)

    xlsx_filename = f'{filename_base}_{size}_xlsx.xlsx'
    save_xlsx(collection, xlsx_filename)

    loaded_pickle = load_pickle(pickle_filename)
    loaded_parquet = load_parquet(parquet_filename)
    loaded_xlsx = load_xlsx(xlsx_filename)

    assert collection == loaded_pickle
    assert collection == loaded_parquet
    assert collection == loaded_xlsx

    print(f"Porównanie dla kolekcji o rozmiarze {size}:")
    print("Moduł pickle - zapis i odczyt: Sukces")
    print("Format Parquet - zapis i odczyt: Sukces")
    print("Format XLSX - zapis i odczyt: Sukces")
    print("-------------")
