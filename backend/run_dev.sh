#!/bin/bash
export PYTHONPATH=./src
gunicorn wsgi:app -b 127.0.0.1:8010 --workers 1 --reload