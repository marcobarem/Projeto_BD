from fpdf import FPDF

# Criar uma classe para o PDF
class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Relatório do Projeto de Banco de Dados', 0, 1, 'C')
        self.ln(10)

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, 0, 1, 'L')
        self.ln(4)

    def chapter_body(self, body):
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, body)
        self.ln()

    def add_chapter(self, title, body):
        self.add_page()
        self.chapter_title(title)
        self.chapter_body(body)

# Criar o documento PDF
pdf = PDF()
pdf.add_page()

# Adicionar conteúdo
pdf.set_font('Arial', 'B', 16)
pdf.cell(0, 10, 'Relatório do Projeto de Banco de Dados', 0, 1, 'C')
pdf.ln(10)

# Introdução
pdf.set_font('Arial', 'B', 14)
pdf.cell(0, 10, 'Introdução', 0, 1, 'L')
pdf.set_font('Arial', '', 12)
pdf.multi_cell(0, 10, 'O objetivo deste projeto é criar e gerenciar um banco de dados para armazenar e analisar dados musicais do Spotify. O banco de dados foi implementado utilizando MongoDB devido à sua flexibilidade e capacidade de manipular grandes volumes de dados não estruturados.')
pdf.ln()

pdf.set_font('Arial', 'B', 14)
pdf.cell(0, 10, 'Justificativa das Escolhas', 0, 1, 'L')
pdf.set_font('Arial', '', 12)
pdf.multi_cell(0, 10, 'Optamos pelo MongoDB por suas características NoSQL que permitem maior flexibilidade na modelagem de dados, escalabilidade horizontal e desempenho superior para grandes volumes de dados. Além disso, a necessidade de operações complexas de leitura e escrita justificou o uso de um banco de dados NoSQL.')
pdf.ln()

pdf.set_font('Arial', 'B', 14)
pdf.cell(0, 10, 'Estrutura do Relatório', 0, 1, 'L')
pdf.set_font('Arial', '', 12)
pdf.multi_cell(0, 10, 'Este relatório está dividido em três seções principais:\n'
                      '1. Introdução: Apresentação do objetivo e justificativas do projeto.\n'
                      '2. Desenvolvimento: Detalhamento da implementação, incluindo modelagem de dados, operações CRUD, segurança, backup e recuperação.\n'
                      '3. Conclusão: Resultados alcançados, desafios enfrentados e sugestões para melhorias futuras.')
pdf.ln()

# Desenvolvimento
pdf.add_page()
pdf.set_font('Arial', 'B', 14)
pdf.cell(0, 10, 'Desenvolvimento', 0, 1, 'L')

# Modelagem de Dados
pdf.set_font('Arial', 'B', 14)
pdf.cell(0, 10, 'Modelagem de Dados', 0, 1, 'L')

pdf.set_font('Arial', 'B', 12)
pdf.cell(0, 10, 'Diagrama ER', 0, 1, 'L')
pdf.set_font('Arial', '', 12)
pdf.multi_cell(0, 10, 'O diagrama ER abaixo ilustra as entidades principais e seus relacionamentos:')
# Adicionar o diagrama ER (Nota: Substitua o caminho pela imagem correta)
# pdf.image('path/to/diagrama_er.png', w=150)
pdf.ln()

pdf.set_font('Arial', 'B', 12)
pdf.cell(0, 10, 'Esquema Relacional Adaptado para MongoDB', 0, 1, 'L')
pdf.set_font('Arial', '', 12)
pdf.multi_cell(0, 10, 'Artistas (artists)\n'
                      '{\n'
                      '  "_id": "artist_id",\n'
                      '  "name": "artist_name",\n'
                      '  "genres": [\n'
                      '    {\n'
                      '      "genre_id": "genre_id",\n'
                      '      "name": "genre_name"\n'
                      '    }\n'
                      '  ]\n'
                      '}\n\n'
                      'Álbuns (albums)\n'
                      '{\n'
                      '  "_id": "album_id",\n'
                      '  "title": "album_title",\n'
                      '  "artist": {\n'
                      '    "artist_id": "artist_id",\n'
                      '    "name": "artist_name"\n'
                      '  },\n'
                      '  "release_date": "release_date",\n'
                      '  "tracks": [\n'
                      '    {\n'
                      '      "track_id": "track_id",\n'
                      '      "title": "track_title",\n'
                      '      "duration_ms": "duration_ms",\n'
                      '      "popularity": "popularity"\n'
                      '    }\n'
                      '  ]\n'
                      '}\n\n'
                      'Músicas (tracks)\n'
                      '{\n'
                      '  "_id": "track_id",\n'
                      '  "title": "track_title",\n'
                      '  "album": {\n'
                      '    "album_id": "album_id",\n'
                      '    "title": "album_title"\n'
                      '  },\n'
                      '  "artist": {\n'
                      '    "artist_id": "artist_id",\n'
                      '    "name": "artist_name"\n'
                      '  },\n'
                      '  "popularity": "popularity",\n'
                      '  "year": "release_year",\n'
                      '  "genre": "genre_name",\n'
                      '  "danceability": "danceability",\n'
                      '  "energy": "energy",\n'
                      '  "key": "key",\n'
                      '  "loudness": "loudness",\n'
                      '  "mode": "mode",\n'
                      '  "speechiness": "speechiness",\n'
                      '  "acousticness": "acousticness",\n'
                      '  "instrumentalness": "instrumentalness",\n'
                      '  "liveness": "liveness",\n'
                      '  "valence": "valence",\n'
                      '  "tempo": "tempo",\n'
                      '  "duration_ms": "duration_ms",\n'
                      '  "time_signature": "time_signature"\n'
                      '}')
pdf.ln()

# Operações CRUD
pdf.set_font('Arial', 'B', 14)
pdf.cell(0, 10, 'Operações CRUD', 0, 1, 'L')

pdf.set_font('Arial', 'B', 12)
pdf.cell(0, 10, 'Inserção de Dados', 0, 1, 'L')
pdf.set_font('Arial', '', 12)
pdf.multi_cell(0, 10, 'Comando SQL Equivalente:\n'
                      'INSERT INTO tracks (track_id, title, album_id, artist_id, popularity, year, genre, danceability, energy, key, loudness, mode, speechiness, acousticness, instrumentalness, liveness, valence, tempo, duration_ms, time_signature) \n'
                      'VALUES (\'1\', \'Track Title 1\', \'1\', \'1\', 85, 2024, \'Genre Name\', 0.8, 0.9, 5, -5.0, 1, 0.04, 0.1, 0.0, 0.2, 0.7, 120.0, 240000, 4);')
pdf.ln()

pdf.set_font('Arial', 'B', 12)
pdf.cell(0, 10, 'Código MongoDB:', 0, 1, 'L')
pdf.set_font('Arial', '', 12)
pdf.multi_cell(0, 10, 'def insert_track(collection, track):\n'
                      '    collection.insert_one(track)')
pdf.ln()

# Consulta de Dados
pdf.set_font('Arial', 'B', 12)
pdf.cell(0, 10, 'Consulta de Dados', 0, 1, 'L')
pdf.set_font('Arial', '', 12)
pdf.multi_cell(0, 10, 'Comando SQL Equivalente:\n'
                      'SELECT title, artist_name, popularity FROM tracks WHERE year = 2024 AND popularity > 80;')
pdf.ln()

pdf.set_font('Arial', 'B', 12)
pdf.cell(0, 10, 'Código MongoDB:', 0, 1, 'L')
pdf.set_font('Arial', '', 12)
pdf.multi_cell(0, 10, 'def query_tracks(collection, year=None, min_popularity=None):\n'
                      '    query = {}\n'
                      '    if year:\n'
                      '        query[\'year\'] = year\n'
                      '    if min_popularity:\n'
                      '        query[\'popularity\'] = {"$gt": min_popularity}\n'
                      '    projection = {"_id": 0, "title": 1, "artist_name": 1, "popularity": 1, "year": 1}\n'
                      '    results = collection.find(query, projection)\n'
                      '    return list(results)')
pdf.ln()

# Atualização de Dados
pdf.set_font('Arial', 'B', 12)
pdf.cell(0, 10, 'Atualização de Dados', 0, 1, 'L')
pdf.set_font('Arial', '', 12)
pdf.multi_cell(0, 10, 'Comando SQL Equivalente:\n'
                      'UPDATE tracks SET popularity = 90 WHERE track_id = \'1\';')
pdf.ln()

pdf.set_font('Arial', 'B', 12)
pdf.cell(0, 10, 'Código MongoDB:', 0, 1, 'L')
pdf.set_font('Arial', '', 12)
pdf.multi_cell(0, 10, 'def update_track(collection, track_id, new_popularity):\n'
                      '    query = {"track_id": track_id}\n'
                      '    update = {"$set": {"popularity": new_popularity}}\n'
                      '    collection.update_one(query, update)')
pdf.ln()

# Exclusão de Dados
pdf.set_font('Arial', 'B', 12)
pdf.cell(0, 10, 'Exclusão de Dados', 0, 1, 'L')
pdf.set_font('Arial', '', 12)
pdf.multi_cell(0, 10, 'Comando SQL Equivalente:\n'
                      'DELETE FROM tracks WHERE track_id = \'1\';')
pdf.ln()

pdf.set_font('Arial', 'B', 12)
pdf.cell(0, 10, 'Código MongoDB:', 0, 1, 'L')
pdf.set_font('Arial', '', 12)
pdf.multi_cell(0, 10, 'def delete_track(collection, track_id):\n'
                      '    query = {"track_id": track_id}\n'
                      '    collection.delete_one(query)')
pdf.ln()

# Implementação de Segurança
pdf.set_font('Arial', 'B', 14)
pdf.cell(0, 10, 'Implementação de Segurança', 0, 1, 'L')

# Controle de Acesso
pdf.set_font('Arial', 'B', 12)
pdf.cell(0, 10, 'Controle de Acesso', 0, 1, 'L')
pdf.set_font('Arial', '', 12)
pdf.multi_cell(0, 10, 'Criação de Usuários:\n'
                      'use admin;\n'
                      'db.createUser({\n'
                      '  user: "admin_user",\n'
                      '  pwd: "admin_password",\n'
                      '  roles: [{ role: "userAdminAnyDatabase", db: "admin" }]\n'
                      '});\n\n'
                      'use spotify;\n'
                      'db.createUser({\n'
                      '  user: "spotify_user",\n'
                      '  pwd: "spotify_password",\n'
                      '  roles: [{ role: "readWrite", db: "spotify" }]\n'
                      '});')
pdf.ln()

pdf.set_font('Arial', 'B', 12)
pdf.cell(0, 10, 'Configuração de Autenticação:', 0, 1, 'L')
pdf.set_font('Arial', '', 12)
pdf.multi_cell(0, 10, 'services:\n'
                      '  mongo:\n'
                      '    image: mongo:4.4-bionic\n'
                      '    container_name: mongo_service\n'
                      '    environment:\n'
                      '      MONGO_INITDB_ROOT_USERNAME: root\n'
                      '      MONGO_INITDB_ROOT_PASSWORD: mongo\n'
                      '    command: ["mongod", "--auth"]\n'
                      '    ports:\n'
                      '      - "27020:27017"\n'
                      '    volumes:\n'
                      '      - dbdata:/data/db\n'
                      '      - ./datasets/musicas:/datasets/musicas\n'
                      '    networks:\n'
                      '      - mybridge\n')
pdf.ln()

# Backup e Recuperação
pdf.set_font('Arial', 'B', 14)
pdf.cell(0, 10, 'Backup e Recuperação', 0, 1, 'L')

pdf.set_font('Arial', 'B', 12)
pdf.cell(0, 10, 'Plano de Backup', 0, 1, 'L')
pdf.set_font('Arial', '', 12)
pdf.multi_cell(0, 10, 'Script de Backup:\n'
                      '#!/bin/bash\n'
                      '# Definir variáveis\n'
                      'BACKUP_DIR="/data/backup"\n'
                      'TIMESTAMP=$(date +%F_%H-%M-%S)\n'
                      'MONGO_HOST="localhost"\n'
                      'MONGO_PORT="27020"\n'
                      'MONGO_DB="spotify"\n'
                      'BACKUP_NAME="backup_$MONGO_DB_$TIMESTAMP"\n\n'
                      '# Criar diretório de backup se não existir\n'
                      'mkdir -p $BACKUP_DIR\n\n'
                      '# Executar mongodump\n'
                      'docker exec mongo_service mongodump --host $MONGO_HOST --port $MONGO_PORT --db $MONGO_DB --out $BACKUP_DIR/$BACKUP_NAME --username root --password mongo --authenticationDatabase admin\n\n'
                      'echo "Backup completo salvo em: $BACKUP_DIR/$BACKUP_NAME"')
pdf.ln()

pdf.set_font('Arial', 'B', 12)
pdf.cell(0, 10, 'Configuração do Cron Job:', 0, 1, 'L')
pdf.set_font('Arial', '', 12)
pdf.multi_cell(0, 10, 'Adicionar ao crontab para execução diária às 2h:\n'
                      'crontab -e\n'
                      '0 2 * * * /path/to/scripts/backup_script.sh')
pdf.ln()

pdf.set_font('Arial', 'B', 12)
pdf.cell(0, 10, 'Plano de Recuperação', 0, 1, 'L')
pdf.set_font('Arial', '', 12)
pdf.multi_cell(0, 10, 'Script de Recuperação:\n'
                      '#!/bin/bash\n'
                      '# Definir variáveis\n'
                      'BACKUP_DIR="/data/backup"\n'
                      'TIMESTAMP="backup_2024-06-24_02-00-00"  # Substitua pelo timestamp do backup que deseja restaurar\n'
                      'MONGO_HOST="localhost"\n'
                      'MONGO_PORT="27020"\n'
                      'MONGO_DB="spotify"\n'
                      'BACKUP_PATH="$BACKUP_DIR/$TIMESTAMP"\n\n'
                      '# Executar mongorestore\n'
                      'docker exec mongo_service mongorestore --host $MONGO_HOST --port $MONGO_PORT --db $MONGO_DB --drop $BACKUP_PATH/$MONGO_DB --username root --password mongo --authenticationDatabase admin\n\n'
                      'echo "Recuperação completa do backup: $BACKUP_PATH"')
pdf.ln()

# Conclusão
pdf.add_page()
pdf.set_font('Arial', 'B', 14)
pdf.cell(0, 10, 'Conclusão', 0, 1, 'L')

pdf.set_font('Arial', 'B', 12)
pdf.cell(0, 10, 'Resultados Alcançados', 0, 1, 'L')
pdf.set_font('Arial', '', 12)
pdf.multi_cell(0, 10, 'O projeto foi bem-sucedido na implementação de um banco de dados flexível e escalável para dados musicais do Spotify, utilizando MongoDB. '
                      'As operações CRUD foram implementadas e integradas com uma interface gráfica utilizando Streamlit, facilitando a interação do usuário com o banco de dados.')
pdf.ln()

pdf.set_font('Arial', 'B', 12)
pdf.cell(0, 10, 'Desafios Enfrentados', 0, 1, 'L')
pdf.set_font('Arial', '', 12)
pdf.multi_cell(0, 10, 'Um dos maiores desafios foi a configuração inicial do Docker e a integração dos serviços. '
                      'Além disso, garantir a segurança e a integridade dos dados foi um aspecto crucial, exigindo uma configuração cuidadosa de autenticação e políticas de backup.')
pdf.ln()

pdf.set_font('Arial', 'B', 12)
pdf.cell(0, 10, 'Soluções Adotadas', 0, 1, 'L')
pdf.set_font('Arial', '', 12)
pdf.multi_cell(0, 10, 'Para superar os desafios, utilizamos boas práticas de configuração de contêineres Docker, implementamos autenticação robusta no MongoDB '
                      'e configuramos backups automáticos para garantir a disponibilidade dos dados.')
pdf.ln()

pdf.set_font('Arial', 'B', 12)
pdf.cell(0, 10, 'Sugestões para Melhorias Futuras', 0, 1, 'L')
pdf.set_font('Arial', '', 12)
pdf.multi_cell(0, 10, 'Para futuras melhorias, recomenda-se a implementação de criptografia em repouso, monitoramento contínuo dos serviços, '
                      'e a expansão das análises de dados com ferramentas de machine learning para fornecer insights mais profundos sobre os dados musicais.')

# Salvar o documento
pdf_output_path = "Relatorio_Projeto_Banco_de_Dados.pdf"
pdf.output(pdf_output_path)

print(f"Relatório gerado com sucesso: {pdf_output_path}")
