# Projeto Todo List com Flask e Docker

## Índice

- Arquitetura do Aplicativo
- Estrutura de Dados
- Como Iniciar o Aplicativo
- Como Usar o Aplicativo
- Estrutura de Arquivos

## Arquitetura do Aplicativo

Este projeto foi construído usando Flask para o backend e utiliza contêineres Docker para o empacotamento da aplicação e do banco de dados PostgreSQL. A arquitetura foi escolhida por ser leve, modular e relativamente fácil de ser implementada.

### Por que Flask?

Flask é um microframework web em Python que é fácil de aprender e rápido para desenvolver. É adequado para pequenas e médias aplicações e permite que tenha-se controle total sobre como expandir a aplicação.

### Por que Docker?

Docker permite que a aplicação seja executada em um ambiente isolado, garantindo o seu funcionamento em qualquer sistema que suporte Docker, independentemente das configurações e versões de sistema local.

## Estrutura de Dados

Para armazenar os dados do usuário e suas tarefas, foi escolhido o banco de dados PostgreSQL.

- Tabela `User`: Armazena informações sobre os usuários.
    - `id`: Identificador único
    - `username`: Nome de usuário
    - `password`: Senha do usuário
- Tabela `Task`: Armazena informações sobre as tarefas.
    - `id`: Identificador único
    - `task`: Descrição da tarefa
    - `status`: Estado da tarefa (completo, incompleto)
    - `user_id`: Chave estrangeira ligada à tabela `User`

### Por que PostgreSQL?

PostgreSQL é um sistema de gerenciamento de banco de dados relacional que é robusto, tem excelente suporte para concorrência e uma variedade de recursos. Ele se integra bem com Python e é uma excelente escolha para aplicações em produção.

## Como Iniciar o Aplicativo

1. Instale o Docker e o Docker-Compose no seu sistema.

2. Clone o repositório:
    `git clone https://github.com/seu_nome/seu_projeto.git`

3. Entre na pasta do projeto:
    `cd seu_projeto`

4. Inicie os serviços usando Docker-Compose:
    `docker-compose up`

5. Acesse o aplicativo em `http://localhost:5000`.

## Como Usar o Aplicativo

- Você será recebido por uma página de login. Insira suas credenciais de usuário.
- Depois de logado, você verá uma lista de suas tarefas atuais. Você pode adicionar ou remover tarefas.

## Estrutura de Arquivos

`|-- backend`

`|   |-- frontend`

`|   |   |-- app.js`

`|   |   |-- Dockerfile`

`|   |   |-- index.html`

`|   |   |-- styles.css`

`|   |-- app.py`

`|   |-- Dockerfile`

`|   |-- requirements.txt`

`|   |-- start.sh`

`|-- docker-compose.yml`

`|-- README.md`

- `backend/`: Contém todo o código do backend, incluindo o arquivo `Dockerfile` para criar a imagem Docker do backend.
- `frontend/`: Contém os arquivos HTML/CSS/JS para a interface do usuário.
- `docker-compose.yml`: Define os serviços, redes e volumes para docker-compose.
