FROM python:3.9-slim

# Diretório de trabalho no container
WORKDIR /app

# Atualizar pip
RUN pip install --upgrade pip

# Copiar e instalar dependências
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o restante do código
COPY . .

# Expor a porta para a aplicação
EXPOSE 5000

# Comando para rodar o app
CMD ["python", "app.py"]
