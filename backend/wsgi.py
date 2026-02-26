import os, sys
print("WSGI FILE:", __file__)
print("CWD:", os.getcwd())
print("PYTHON:", sys.executable)

from src.op_app.app import create_app
app = create_app()
print("APP CREATED OK")