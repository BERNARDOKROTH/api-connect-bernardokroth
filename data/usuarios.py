usuarios = [
    {
        "id": 1,
        "nome": "João Silva",
        "email": "joao@email.com"
    },
    {
        "id": 2,
        "nome": "Maria Souza",
        "email": "maria@email.com"
    }
]

proximo_id = 3


def gerar_id():
    global proximo_id

    novo_id = proximo_id
    proximo_id += 1

    return novo_id
