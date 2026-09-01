from flask import Blueprint

from controllers.usuarios_controller import (
    listar_usuarios,
    buscar_usuario,
    cadastrar_usuario,
    atualizar_usuario,
    excluir_usuario
)

usuarios_bp = Blueprint("usuarios", __name__)


@usuarios_bp.route("/usuarios", methods=["GET"])
def rota_listar_usuarios():
    return listar_usuarios()


@usuarios_bp.route("/usuarios/<int:id>", methods=["GET"])
def rota_buscar_usuario(id):
    return buscar_usuario(id)


@usuarios_bp.route("/usuarios", methods=["POST"])
def rota_cadastrar_usuario():
    return cadastrar_usuario()


@usuarios_bp.route("/usuarios/<int:id>", methods=["PUT"])
def rota_atualizar_usuario(id):
    return atualizar_usuario(id)


@usuarios_bp.route("/usuarios/<int:id>", methods=["DELETE"])
def rota_excluir_usuario(id):
    return excluir_usuario(id)
