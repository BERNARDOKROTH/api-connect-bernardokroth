# API Connect

A API Connect é uma API simples para gerenciamento de usuários, desenvolvida como um MVP para uma atividade prática de desenvolvimento back-end.

O sistema permite cadastrar, listar, buscar, atualizar e excluir usuários.

## Tecnologias utilizadas

* Python
* Flask
* JSON
* GitHub
* API REST

## Estrutura do projeto

```text
api-connect/
│
├── app.py
├── requirements.txt
├── .gitignore
├── README.md
│
├── routes/
│   └── usuarios_routes.py
│
├── controllers/
│   └── usuarios_controller.py
│
└── data/
    └── usuarios.py
```

## Como executar o projeto

Para executar o projeto localmente, é necessário possuir o Python instalado.

Primeiro, crie um ambiente virtual:

```bash
python -m venv venv
```

No Windows, ative o ambiente virtual:

```bash
venv\Scripts\activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute a aplicação:

```bash
python app.py
```

O servidor será iniciado no endereço:

```text
http://127.0.0.1:5000
```

## Endpoints

| Método | Endpoint         | Função                   |
| ------ | ---------------- | ------------------------ |
| GET    | `/usuarios`      | Lista todos os usuários  |
| GET    | `/usuarios/<id>` | Busca um usuário pelo ID |
| POST   | `/usuarios`      | Cadastra um novo usuário |
| PUT    | `/usuarios/<id>` | Atualiza um usuário      |
| DELETE | `/usuarios/<id>` | Exclui um usuário        |

## Exemplo de cadastro

Método:

```text
POST
```

Endpoint:

```text
/usuarios
```

JSON enviado:

```json
{
    "nome": "Carlos Silva",
    "email": "carlos@email.com"
}
```

Em caso de sucesso, a API retorna o código:

```text
201 Created
```

## Códigos de status

`200 OK` indica que a operação foi realizada com sucesso.

`201 Created` indica que um novo usuário foi cadastrado.

`400 Bad Request` indica que os dados enviados estão incompletos ou incorretos.

`404 Not Found` indica que o usuário solicitado não foi encontrado.

## Armazenamento dos dados

Nesta versão do projeto, os usuários são armazenados em uma lista na memória do servidor. Essa solução foi utilizada por se tratar de um MVP e não exigir um banco de dados nesta etapa.

Os usuários possuem os campos `id`, `nome` e `email`.

## Objetivo

O projeto foi desenvolvido para aplicar na prática conceitos de desenvolvimento back-end, criação de APIs, métodos HTTP, formato JSON, validação de dados, organização de código e gerenciamento de usuários.
