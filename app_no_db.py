from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Geçici veri depolama
firms = []

@app.route('/')
def home():
    return "Flask uygulaması çalışıyor! API rotaları: /firms"

@app.route('/firms', methods=['POST'])
def add_firm():
    data = request.json
    data['id'] = len(firms) + 1
    firms.append(data)
    return jsonify({"message": "Firma başarıyla eklendi", "firm": data}), 201

@app.route('/firms', methods=['GET'])
def list_firms():
    return jsonify(firms), 200

@app.route('/firms/<int:id>', methods=['PUT'])
def update_firm(id):
    data = request.json
    for firm in firms:
        if firm['id'] == id:
            firm.update(data)
            return jsonify({"message": "Firma başarıyla güncellendi", "firm": firm}), 200
    return jsonify({"error": "Firma bulunamadı"}), 404

@app.route('/firms/<int:id>', methods=['DELETE'])
def delete_firm(id):
    global firms
    firms = [firm for firm in firms if firm['id'] != id]
    return jsonify({"message": "Firma başarıyla silindi"}), 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
