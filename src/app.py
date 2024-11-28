from flask import Flask, request, jsonify  # type: ignore
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)

# Configuração do Prometheus para expor métricas
metrics = PrometheusMetrics(app)

# Rota de teste
@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Bem-vindo ao Sistema de Cadastro de Alunos!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
