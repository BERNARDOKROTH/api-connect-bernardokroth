
from flask import Flask, request, jsonify
from routes.usuarios_routes import usuarios_bp

app = Flask(__name__)


# Verifica se os dados de POST e PUT estão em JSON
@app.before_request
def verificar_json():
    if request.method in ["POST", "PUT", "PATCH"] and not request.is_json:
        return jsonify({
            "error": "O corpo da requisição deve estar em formato JSON"
        }), 400


# Rota inicial para testar a API
@app.route("/", methods=["GET"])
def inicio():
    return jsonify({
        "data": {
            "mensagem": "API Connect funcionando corretamente"
        }
    }), 200


# Registra as rotas dos usuários
app.register_blueprint(usuarios_bp)


if __name__ == "__main__":
    app.run(port=5000, debug=True)
