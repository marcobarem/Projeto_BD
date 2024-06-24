# src/load_data.py
import pymongo
import pandas as pd

def get_database():
    client = pymongo.MongoClient("mongodb://root:mongo@mongo_service:27017/")
    return client["spotify"]

def load_data_from_csv(file_path, collection_name):
    db = get_database()
    collection = db[collection_name]
    data = pd.read_csv(file_path)
    data_dict = data.to_dict("records")
    collection.insert_many(data_dict)

def main():
    import time
    time.sleep(10)  # Espera MongoDB inicializar

    load_data_from_csv("/datasets/musicas/spotify_data_corrigido_UTF8.csv", "tracks")

    print("Dados inseridos com sucesso!")

if __name__ == "__main__":
    main()
