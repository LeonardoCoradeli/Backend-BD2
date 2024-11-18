# Sistema Backend de Gerenciamento de Decks e Cartas

## Visão Geral

Este sistema backend foi projetado para gerenciar decks de cartas colecionáveis, rastrear interações de cartas e analisar sinergias. Ele oferece endpoints para criar, atualizar e recuperar informações sobre cartas, decks, temas e preços de cartas. O backend utiliza FastAPI para uma estrutura de API escalável e MySQL para persistência de dados.

## Funcionalidades

- **Gerenciamento de Decks**: Criar, atualizar, excluir e recuperar decks e suas cartas associadas.
- **Gerenciamento de Cartas**: Gerenciar cartas, incluindo seus atributos, histórico de preços e interações.
- **Análise de Sinergia**: Calcular e armazenar pontuações de sinergia para decks.
- **Rastreamento de Preços**: Registrar e recuperar o histórico de preços das cartas.

## Pré-requisitos

Antes de executar este projeto, certifique-se de ter os seguintes requisitos:

- Python 3.8 ou superior
- MySQL ou um banco de dados relacional compatível
- Ferramenta de ambiente virtual (recomendado)

## Instalação

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/Backend-BD2.git
cd Backend-BD2
```

### 2. Configure um ambiente virtual (opcional, mas recomendado)

```bash
# No Windows
python -m venv venv
venv\Scripts\activate

# No macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Configure o ambiente

Crie um arquivo `.env` no diretório raiz com o seguinte conteúdo (ajuste os valores conforme necessário):

```env
DATABASE_URL="mysql+aiomysql://usuario:senha@localhost:3305/nome_do_banco_de_dados"
```

- Substitua `usuario`, `senha`, `localhost`, `3305` e `nome_do_banco_de_dados` pela sua configuração MySQL.

### 5. Inicialize o banco de dados

Certifique-se de que seu banco de dados MySQL está em execução e inicializado com o esquema necessário. Você pode usar um script de inicialização ou configurar as tabelas manualmente com base nos modelos do projeto.

## Executando o Backend

Para iniciar o servidor backend, execute o seguinte comando:

```bash
uvicorn app.main:app --reload
```

O servidor estará acessível em `http://127.0.0.1:8000/`.

### Acessando a Documentação da API

- **Swagger UI**: `http://127.0.0.1:8000/docs`
- **ReDoc**: `http://127.0.0.1:8000/redoc`

Essas páginas de documentação fornecem uma maneira interativa de explorar e testar os endpoints da API.

## Estrutura do Projeto

- `app/`
  - `api/v1/`: Contém definições de rotas para diferentes funcionalidades (ex.: cartas, decks, usuários).
  - `core/`: Configurações principais, incluindo configuração do banco de dados.
  - `services/`: Contém a lógica de negócios para lidar com diferentes operações.
  - `data/`: Repositórios para interações com o banco de dados.
  - `domain/`: Modelos Pydantic que representam as estruturas de dados usadas no projeto.

---

### Exemplo de Uso

1. **Criar um Usuário**: Use o endpoint `/users/` para criar um novo usuário.
2. **Gerenciar Cartas e Decks**: Acesse os endpoints para criar, atualizar, excluir e listar cartas e decks.

### Licença

Este projeto está licenciado sob a Licença MIT.

---

# Deck and Card Management Backend System

## Overview

This backend system is designed for managing collectible card decks, tracking card interactions, and analyzing synergies. It offers endpoints for creating, updating, and retrieving information about cards, decks, themes, and card prices. The backend uses FastAPI for a scalable API structure and MySQL for data persistence.

## Features

- **Deck Management**: Create, update, delete, and retrieve decks and their associated cards.
- **Card Management**: Manage cards, including their attributes, pricing history, and interactions.
- **Synergy Analysis**: Calculate and store synergy scores for decks.
- **Price Tracking**: Record and retrieve the price history of cards.

## Prerequisites

Before running this project, ensure you have the following:

- Python 3.8 or higher
- MySQL or a compatible relational database
- Virtual environment tool (recommended)

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/seu-usuario/Backend-BD2.git
cd Backend-BD2
```

### 2. Set up a virtual environment (optional but recommended)

```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the environment

Create a `.env` file in the root directory with the following content (adjust values as needed):

```env
DATABASE_URL="mysql+aiomysql://user:password@localhost:3305/your_database_name"
```

- Replace `user`, `password`, `localhost`, `3305`, and `your_database_name` with your actual MySQL configuration.

### 5. Initialize the database

Ensure your MySQL database is running and initialized with the required schema. You can use an initialization script or manually set up the tables based on the project's models.

## Running the Backend

To start the backend server, run the following command:

```bash
uvicorn app.main:app --reload
```

The server will start and be accessible at `http://127.0.0.1:8000/`.

### Accessing the API Documentation

- **Swagger UI**: `http://127.0.0.1:8000/docs`
- **ReDoc**: `http://127.0.0.1:8000/redoc`

These documentation pages provide an interactive way to explore and test the API endpoints.

## Project Structure

- `app/`
  - `api/v1/endpoints/`: Contains route definitions for different features (e.g., cards, decks, users).
  - `core/`: Core configurations, including database setup.
  - `services/`: Contains business logic for handling different operations.
  - `data/`: Repositories for database interactions.
  - `domain/`: Pydantic models representing the data structures used throughout the project.

---

### Example Usage

1. **Create a User**: Use the `/users/` endpoint to create a new user.
2. **Manage Cards and Decks**: Access endpoints to create, update, delete, and list cards and decks.

### License

This project is licensed under the MIT License.
