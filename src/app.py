from flask import Flask, request, jsonify  # type: ignore
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)

# Lista para armazenar alunos
students = []

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Bem-vindo ao Sistema de Cadastro de Alunos!"})

@app.route("/students", methods=["POST"])
def register_student():
    data = request.json
    if not data.get("name") or not data.get("registration_number"):
        return jsonify({"error": "Os campos 'name' e 'registration_number' são obrigatórios."}), 400
    student = {
        "name": data["name"],
        "registration_number": data["registration_number"]
    }
    students.append(student)
    return jsonify({"message": "Aluno cadastrado com sucesso!", "student": student}), 201

@app.route("/students", methods=["GET"])
def list_students():
    return jsonify(students)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)