import os, sys
print("WSGI FILE:", __file__)
print("CWD:", os.getcwd())
print("PYTHON:", sys.executable)

print("1. entrou no wsgi")

from src.op_app.app import create_app
print("2. importou create_app")

app = create_app()
print("3. app criada")
print("*"*30)
print("APP CREATED OK")