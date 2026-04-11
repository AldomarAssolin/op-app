# Usa imagem leve do Python
FROM python:3.11-slim

# Evita aquelas frescuras de buffer
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Diretório dentro do container
WORKDIR /app

# Copia dependências primeiro (melhor cache)
COPY requirements.txt .

# Instala dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante do projeto
COPY . .

# Porta da aplicação
EXPOSE 8000

# Comando padrão (ajuste conforme seu app)
CMD ["gunicorn", "-c", "gunicorn.conf.py", "wsgi:app"]