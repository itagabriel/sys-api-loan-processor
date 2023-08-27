
# [LFG] Challenge - Plataforma de Empréstimo

Este é o README do projeto que visa criar uma plataforma que permite que os solicitantes preencham propostas de empréstimo online. As propostas serão avaliadas automaticamente por meio de uma API de Análise de Crédito, e as propostas aprovadas serão disponibilizadas para avaliação humana.

## Funcionalidades Principais

-   Cadastro de campos da proposta pelo administrador através do django-admin.
-   Preenchimento da proposta pelos usuários através de uma página de preenchimento.
-   Comunicação entre frontend e backend através do Django Rest Framework.
-   Envio da proposta para uma fila RabbitMQ após o preenchimento.
-   Avaliação da proposta pela API externa
-   Atualização do status da proposta no banco de dados após a avaliação feita pela API externa incorporada pelo Django Celery.
-   Visualização das propostas cadastradas no admin-django, com indicação de status.

##  Tecnologias Utilizadas

- Python: 3.11.3
- Django: 4.2.2
- Django Rest Framework: 3.14.0
- Django Celery: 5.3.1
- RabbitMQ: 5.1.1
- PostgreSQL: 13.11
- API de Análise de Crédito: https://loan-processor.digitalsys.com.br/swagger/index.html

## Pré-requisitos

Certifique-se de ter os seguintes softwares instalados em seu ambiente de desenvolvimento:

- Docker e Docker Compose

## Configuração do Ambiente

O projeto utiliza Docker para facilitar a configuração do ambiente de desenvolvimento. Certifique-se de ter o Docker instalado em sua máquina antes de prosseguir.

Documentação do Docker para instalação
https://docs.docker.com/engine/install/

### Passos para configurar o ambiente:

1. Clone este repositório em sua máquina local:
>* $ git clone https://github.com/itagabriel/system-api-loan-processor.git

2. Acesse o diretório do projeto:
>* $ cd system-api-loan-processor

3. Execute o comando a seguir para construir as imagens e iniciar os containers:
>* $ docker-compose build && docker-compose up -d
>* $ docker-compose ps or docker ps (ambos os comandos irão listar os containers)

Isso irá baixar as imagens necessárias, criar os containers e iniciar o sistema. Aguarde até que todos os serviços estejam prontos para uso.

4. O sistema estará disponível nos seguintes endereços:
>* Aplicação Web (Formulário de Proposta): http://localhost:8000
>* Administração do Django: http://localhost:8000/admin
>* Você pode acessar essas URLs em seu navegador para interagir com o sistema. 
>* RabbitMQ Management: http://localhost:15672/
>* Verifique as credenciais no arquivo: django_app\\credentials.txt

5. Para acessar a base de dados é necessário alguns comandos:
>* $ docker exec -it psql sh
>* $ psql -U sys_admin -d sys_gestao_proposta_emprestimo -h psql -p 5432
>*  Insira o password da base de dados
>* Verifique as credenciais do PSQL no arquivo: django_app\\credentials.txt

6. Para encerrar a execução do sistema, utilize o comando a seguir no diretório do projeto:

>* $ docker-compose stop

7. Para derrubar os containers na sua aplicação, utilize o comando a seguir no diretório do projeto:
>* $ docker-compose down --volumes

## Testes

Foram implementados testes unitários para verificar o funcionamento correto dos campos do formulário. Para executar os testes, certifique-se de estar no diretório do projeto e execute o seguinte comando:

>* $ docker exec -it django sh
>* $ python manage.py test

## Autor

Obrigado por conferir este projeto! Desenvolvi este sistema como parte de um desafio técnico. Se você tiver alguma dúvida ou sugestão relacionada a este projeto, sinta-se à vontade para entrar em contato comigo.

**Autor:** Gabriel Ita

**Contato:** ita32.gabriel@gmail.com

**GitHub:** https://github.com/itagabriel