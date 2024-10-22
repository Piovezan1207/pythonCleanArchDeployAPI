# Usar uma imagem base do Python
FROM python:3.9-slim

# Atualizar os pacotes do sistema e instalar o at e cron
RUN apt-get update && apt-get install -y at cron && apt-get install -y curl

# Criar o diretório de trabalho
WORKDIR /app

# Copiar os arquivos necessários (seu script Python e outros)
COPY . /app

# Instalar as dependências do Python listadas no requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Garantir que o atd seja iniciado ao rodar o container
# O 'tail -f /dev/null' mantém o container rodando indefinidamente
CMD service atd start && gunicorn -w 5 --timeout 180 -b 0.0.0.0:5000 main:app && tail -f /dev/null
