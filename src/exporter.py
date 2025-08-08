from datetime import datetime
import os
import csv

def save_to_csv(df, query):
    file_name = f"data/press_search_{query}.csv"
    os.makedirs("data",exist_ok=True)
    df.to_csv(file_name,index=False)
    print(f"Exported results to {file_name}")







