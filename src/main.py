# src/main.py
import streamlit as st
import pandas as pd
from db_connection import get_database
from crud_operations import insert_track, query_tracks, update_track, delete_track

# Configurar Streamlit
st.set_page_config(layout="wide")
st.title("Análise de Dados Musicais do Spotify")

# Conectar ao MongoDB
db = get_database()
if db is None:
    st.error("Falha na conexão ao servidor MongoDB")
else:
    st.success("Conexão estabelecida com sucesso!")
    collection = db['tracks']

    # Funções CRUD
    def insert_data():
        st.subheader("Inserir Nova Música")
        with st.form(key='insert_form'):
            track_id = st.text_input("ID da Música")
            title = st.text_input("Título")
            artist_id = st.text_input("ID do Artista")
            album_id = st.text_input("ID do Álbum")
            artist_name = st.text_input("Nome do Artista")
            genre = st.text_input("Gênero")
            year = st.number_input("Ano", min_value=1900, max_value=2100, value=2024)
            popularity = st.slider("Popularidade", min_value=0, max_value=100, value=50)
            danceability = st.slider("Danceabilidade", min_value=0.0, max_value=1.0, value=0.5)
            energy = st.slider("Energia", min_value=0.0, max_value=1.0, value=0.5)
            acousticness = st.slider("Acousticidade", min_value=0.0, max_value=1.0, value=0.5)
            speechiness = st.slider("Fala", min_value=0.0, max_value=1.0, value=0.5)
            instrumentalness = st.slider("Instrumentalidade", min_value=0.0, max_value=1.0, value=0.0)
            loudness = st.number_input("Volume (dB)", min_value=-60.0, max_value=0.0, value=-5.0)
            tempo = st.number_input("Tempo (BPM)", min_value=0, max_value=300, value=120)
            duration_ms = st.number_input("Duração (ms)", min_value=0, value=180000)
            time_signature = st.number_input("Compasso", min_value=1, max_value=12, value=4)
            mode = st.selectbox("Modo", options=[0, 1])

            submit_button = st.form_submit_button(label='Inserir Música')

            if submit_button:
                new_track = {
                    "track_id": track_id,
                    "title": title,
                    "artist_id": artist_id,
                    "album_id": album_id,
                    "artist_name": artist_name,
                    "genre": genre,
                    "year": year,
                    "popularity": popularity,
                    "danceability": danceability,
                    "energy": energy,
                    "acousticness": acousticness,
                    "speechiness": speechiness,
                    "instrumentalness": instrumentalness,
                    "loudness": loudness,
                    "tempo": tempo,
                    "duration_ms": duration_ms,
                    "time_signature": time_signature,
                    "mode": mode
                }
                insert_track(collection, new_track)
                st.success("Música inserida com sucesso!")

    def consult_data():
        st.subheader("Consultar Músicas")
        search_by = st.selectbox("Buscar por", ["ID da Música", "Nome da Música"])
        if search_by == "ID da Música":
            track_id = st.text_input("ID da Música")
            query_button = st.button("Consultar Músicas")
            if query_button:
                query = {"track_id": track_id}
                results = query_tracks(collection, query)
                df = pd.DataFrame(results)
                st.write(df)
        elif search_by == "Nome da Música":
            track_title = st.text_input("Título da Música")
            query_button = st.button("Consultar Músicas")
            if query_button:
                query = {"title": track_title}
                results = query_tracks(collection, query)
                df = pd.DataFrame(results)
                st.write(df)

    def update_data():
        st.subheader("Atualizar Popularidade da Música")
        search_by = st.selectbox("Buscar por", ["ID da Música", "Nome da Música"])
        if search_by == "ID da Música":
            track_id = st.text_input("ID da Música para Atualizar")
            new_title = st.text_input("Novo Título da Música")
            update_button = st.button("Atualizar Título")
            if update_button:
                filter_query = {"track_id": track_id}
                update_query = {"title": new_title}
                update_track(collection, filter_query, update_query)
                st.success("Título da música atualizado com sucesso!")
        elif search_by == "Nome da Música":
            track_title = st.text_input("Título da Música para Atualizar")
            new_title = st.text_input("Novo Título da Música")
            update_button = st.button("Atualizar Título")
            if update_button:
                filter_query = {"title": track_title}
                update_query = {"title": new_title}
                update_track(collection, filter_query, update_query)
                st.success("Título da música atualizado com sucesso!")

    def delete_data():
        st.subheader("Excluir Música")
        track_id = st.text_input("ID da Música para Excluir")
        delete_button = st.button("Excluir Música")
        if delete_button:
            delete_track(collection, {"track_id": track_id})
            st.success("Música excluída com sucesso!")

    # Interface do Usuário
    option = st.sidebar.selectbox(
        "Escolha a operação:",
        ["Inserir Dados", "Consultar Dados", "Atualizar Dados", "Excluir Dados"]
    )

    if option == "Inserir Dados":
        insert_data()
    elif option == "Consultar Dados":
        consult_data()
    elif option == "Atualizar Dados":
        update_data()
    elif option == "Excluir Dados":
        delete_data()
