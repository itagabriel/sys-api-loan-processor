import os
from celery import Celery

# Define o nome do projeto Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_project.settings')

# Cria a instância do objeto Celery
app = Celery('django_project')

# Configura as opções do Celery
app.config_from_object('django.conf:settings', namespace='CELERY')

# Configura tentativas de reconexão durante a inicialização
app.conf.broker_connection_retry_on_startup = True

# Carrega as tasks do projeto
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')