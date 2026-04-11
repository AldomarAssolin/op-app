#!/bin/sh

echo "Esperando banco subir..."
sleep 5

echo "Rodando migrations..."
alembic upgrade head

echo "Iniciando aplicação..."
exec "$@"