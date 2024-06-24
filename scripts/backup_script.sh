#!/bin/bash

# Definir variáveis
BACKUP_DIR="/data/backup"
TIMESTAMP=$(date +%F_%H-%M-%S)
MONGO_HOST="localhost"
MONGO_PORT="27020"
MONGO_DB="spotify"
BACKUP_NAME="backup_$MONGO_DB_$TIMESTAMP"

# Criar diretório de backup se não existir
mkdir -p $BACKUP_DIR

# Executar mongodump
docker exec mongo_service mongodump --host $MONGO_HOST --port $MONGO_PORT --db $MONGO_DB --out $BACKUP_DIR/$BACKUP_NAME --username root --password mongo --authenticationDatabase admin

echo "Backup completo salvo em: $BACKUP_DIR/$BACKUP_NAME"
