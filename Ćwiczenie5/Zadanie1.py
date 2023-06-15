import os
import pickle
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
from openpyxl import Workbook

def save_pickle(data, filename):
    with open(filename, 'wb') as file:
        pickle.dump(data, file)

def load_pickle(filename):
    with open(filename, 'rb') as file:
        data = pickle.load(file)
    return data

def save_parquet(data, filename):
    df = pd.DataFrame(data)
    table = pa.Table.from_pandas(df)
    pq.write_table(table, filename)

def load_parquet(filename):
    table = pq.read_table(filename)
    df = table.to_pandas()
    data = df.to_dict(orient='records')
    return data

def save_xlsx(data, filename):
    wb = Workbook()
    ws = wb.active

    for i, item in enumerate(data, start=1):
        for j, value in enumerate(item.values(), start=1):
            ws.cell(row=i, column=j, value=value)

    wb.save(filename)

def load_xlsx(filename):
    wb = pd.read_excel(filename)
    data = wb.to_dict(orient='records')
    return data

# Przykładowa kolekcja danych
collection = [{'id': i, 'value': i*2} for i in range(1, 101)]

# Zapisywanie i odczytywanie kolekcji za pomocą modułu pickle
save_pickle(collection, 'collection.pickle')
loaded_pickle = load_pickle('collection.pickle')

# Zapisywanie i odczytywanie kolekcji za pomocą Parquet
save_parquet(collection, 'collection.parquet')
loaded_parquet = load_parquet('collection.parquet')

# Zapisywanie i odczytywanie kolekcji za pomocą XLSX
save_xlsx(collection, 'collection.xlsx')
loaded_xlsx = load_xlsx('collection.xlsx')

print(f"Liczba elementów w kolekcji: {len(collection)}")
print("Moduł pickle:")
print(f"   Zapis: {len(pickle.dumps(collection))} bajtów")
print(f"   Odczyt: {len(pickle.dumps(loaded_pickle))} bajtów")
print("Parquet:")
print(f"   Zapis: {os.path.getsize('collection.parquet')} bajtów")
print(f"   Odczyt: {os.path.getsize('collection.parquet')} bajtów")
print("XLSX:")
print(f"   Zapis: {os.path.getsize('collection.xlsx')} bajtów")
print(f"   Odczyt: {os.path.getsize('collection.xlsx')} bajtów")
