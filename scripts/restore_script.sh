#!/bin/bash

# Definir variáveis
BACKUP_DIR="/data/backup"
TIMESTAMP="backup_2024-06-24_02-00-00"  # Substitua pelo timestamp do backup que deseja restaurar
MONGO_HOST="localhost"
MONGO_PORT="27020"
MONGO_DB="spotify"
BACKUP_PATH="$BACKUP_DIR/$TIMESTAMP"

# Executar mongorestore
docker exec mongo_service mongorestore --host $MONGO_HOST --port $MONGO_PORT --db $MONGO_DB --drop $BACKUP_PATH/$MONGO_DB --username root --password mongo --authenticationDatabase admin

echo "Recuperação completa do backup: $BACKUP_PATH"
