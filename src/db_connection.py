# src/db_connection.py
import pymongo
from pymongo.errors import ConnectionFailure

def get_database():
    try:
        client = pymongo.MongoClient("mongodb://spotify_user:spotify_password@localhost:27020/?authSource=spotify")
        client.server_info()  # Isso lançará uma exceção se não puder se conectar ao servidor.
        print("Conexão estabelecida com sucesso!")
        return client['spotify']
    except ConnectionFailure:
        print("Falha na conexão ao servidor MongoDB")
        return None
