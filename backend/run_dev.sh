#!/bin/bash
export PYTHONPATH=./src
# O 'exec' ajuda no gerenciamento de sinais do sistema
exec gunicorn wsgi:app -b 127.0.0.1:8010 --workers 1 --reload