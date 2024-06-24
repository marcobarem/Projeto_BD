# Análise de Dados Musicais do Spotify

## Descrição do Projeto

Este projeto tem como objetivo criar e gerenciar um banco de dados para armazenar e analisar dados musicais do Spotify. O banco de dados foi implementado utilizando MongoDB devido à sua flexibilidade e capacidade de manipular grandes volumes de dados não estruturados.

## Estrutura do Projeto

```PROJETO_BD/
├── mongodb/
│ ├── datasets/musicas/
│ │ └── spotify_data_corrigido_UTF8.csv
│ ├── db-seed/
│ ├── admin.txt
│ ├── docker-compose.yml
│ ├── user.txt
│ ├── wait-for-it.sh
├── scripts/
│ ├── backup_script.sh
│ ├── restore_script.sh
├── src/
│ ├── init.py
│ ├── crud_operations.py
│ ├── db_connection.py
│ ├── load_data.py
│ ├── main.py
├── README.md
```


## Tecnologias Utilizadas

- **MongoDB:** Banco de dados NoSQL utilizado para armazenar os dados musicais.
- **Docker:** Ferramenta utilizada para containerização do ambiente de desenvolvimento e do banco de dados.
- **Streamlit:** Framework utilizado para construir a interface web para interagir com o banco de dados.
- **Python:** Linguagem de programação utilizada para implementar as funcionalidades do projeto.

## Instalação e Configuração

### Pré-requisitos

- Docker instalado na máquina.
- Python 3.6+ instalado na máquina.
- Biblioteca `streamlit` instalada: `pip install streamlit`
- Biblioteca `pymongo` instalada: `pip install pymongo`

### Passos para Configuração

1. **Clone o repositório do projeto:**

   ```bash
   git clone https://github.com/marcobarem/Projeto_BD.git
   cd PROJETO_BD
    ```

Inicie os contêineres do Docker:
    `docker-compose up -d`

Carregue os dados no MongoDB, se necessário (opcional):
    `docker exec -it mongo_service mongoimport --db spotify --collection musicas --type csv --file /datasets/musicas/spotify_data_corrigido_UTF8.csv --headerline --ignoreBlanks --username root --password mongo --authenticationDatabase admin`


Execute o Streamlit:
    `streamlit run src/main.py`

Funcionalidades
Inserir Dados
Permite ao usuário inserir novas músicas no banco de dados através de um formulário na interface web.

Consultar Dados
Permite ao usuário consultar músicas no banco de dados utilizando filtros como ID da música ou nome da música.

Atualizar Dados
Permite ao usuário atualizar os dados de uma música específica, utilizando o ID da música ou o nome da música como critério de busca.

Excluir Dados
Permite ao usuário excluir uma música específica do banco de dados utilizando o ID da música.

Scripts de Backup e Recuperação
Backup
O script backup_script.sh é utilizado para realizar backups dos dados do MongoDB.

Recuperação
O script restore_script.sh é utilizado para restaurar os dados a partir de um backup previamente realizado.

Relatório do Projeto
O relatório do projeto detalha todos os aspectos do desenvolvimento, incluindo justificativas para as escolhas feitas, desafios enfrentados e soluções adotadas. O relatório também inclui um diagrama ER, esquema relacional adaptado para MongoDB, exemplos de operações CRUD e a implementação de políticas de segurança.

Contribuição
Para contribuir com o projeto, faça um fork do repositório, crie um branch para suas modificações e envie um pull request detalhando as mudanças propostas.    