from flask import request, jsonify
from data.usuarios import usuarios, gerar_id


# Listar todos os usuários
def listar_usuarios():
    return jsonify({
        "data": usuarios
    }), 200


# Buscar usuário pelo ID
def buscar_usuario(id):
    usuario = next(
        (usuario for usuario in usuarios if usuario["id"] == id),
        None
    )

    if usuario is None:
        return jsonify({
            "error": "Usuário não encontrado"
        }), 404

    return jsonify({
        "data": usuario
    }), 200


# Cadastrar usuário
def cadastrar_usuario():
    dados = request.get_json(silent=True)

    if not dados:
        return jsonify({
            "error": "Nenhum dado foi enviado"
        }), 400

    if "nome" not in dados or not dados["nome"]:
        return jsonify({
            "error": "O campo nome é obrigatório"
        }), 400

    if "email" not in dados or not dados["email"]:
        return jsonify({
            "error": "O campo email é obrigatório"
        }), 400

    novo_usuario = {
        "id": gerar_id(),
        "nome": dados["nome"],
        "email": dados["email"]
    }

    usuarios.append(novo_usuario)

    return jsonify({
        "data": novo_usuario
    }), 201


# Atualizar usuário
def atualizar_usuario(id):
    usuario = next(
        (usuario for usuario in usuarios if usuario["id"] == id),
        None
    )

    if usuario is None:
        return jsonify({
            "error": "Usuário não encontrado"
        }), 404

    dados = request.get_json(silent=True)

    if not dados:
        return jsonify({
            "error": "Nenhum dado foi enviado"
        }), 400

    if "nome" not in dados or not dados["nome"]:
        return jsonify({
            "error": "O campo nome é obrigatório"
        }), 400

    if "email" not in dados or not dados["email"]:
        return jsonify({
            "error": "O campo email é obrigatório"
        }), 400

    usuario["nome"] = dados["nome"]
    usuario["email"] = dados["email"]

    return jsonify({
        "data": usuario
    }), 200


# Excluir usuário
def excluir_usuario(id):
    usuario = next(
        (usuario for usuario in usuarios if usuario["id"] == id),
        None
    )

    if usuario is None:
        return jsonify({
            "error": "Usuário não encontrado"
        }), 404

    usuarios.remove(usuario)

    return jsonify({
        "data": {
            "mensagem": "Usuário removido com sucesso"
        }
    }), 200
