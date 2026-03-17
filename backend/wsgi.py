import os, sys
from src.op_app.app import create_app

print("WSGI FILE:", __file__)
print("CWD:", os.getcwd())
print("PYTHON:", sys.executable)

app = create_app()
print("APP CREATED OK")