#!/bin/sh

# O shell irá encerrar a execução do script quando um comando falhar
set -e

# Aguardar a inicialização do PostgreSQL
while ! nc -z psql 5432; do
  echo "🟡 Waiting for Postgres Database Startup..."
  sleep 2
done

echo "✅ Postgres Database Started Successfully ($POSTGRES_HOST:$POSTGRES_PORT)"

# Executar os comandos do Django
python manage.py collectstatic --noinput
python manage.py makemigrations --noinput
python manage.py migrate --noinput

# Verificar se o superusuário já existe no banco de dados
if [ "$(python manage.py shell -c 'from django.contrib.auth.models import User; print(User.objects.filter(username="administrator").exists())')" == "False" ]; then
  # Criação do superusuário
  echo "🟢 Creating Django superuser..."
  python manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('administrator', 'admin@example.com', 'administrator')"
fi

# Iniciar o servidor Django
python manage.py runserver 0.0.0.0:8000