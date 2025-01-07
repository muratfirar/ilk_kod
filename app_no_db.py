from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Geçici veri depolama (örnek veriler RAM'de tutulur)
firms = []

@app.route('/firms', methods=['POST'])
def add_firm():
    """Yeni firma ekler."""
    data = request.json
    data['id'] = len(firms) + 1  # Otomatik ID
    firms.append(data)
    return jsonify({"message": "Firma başarıyla eklendi", "firm": data}), 201

@app.route('/firms', methods=['GET'])
def list_firms():
    """Tüm firmaları listeler."""
    return jsonify(firms), 200

@app.route('/firms/<int:id>', methods=['PUT'])
def update_firm(id):
    """Firma bilgilerini günceller."""
    data = request.json
    for firm in firms:
        if firm['id'] == id:
            firm.update(data)
            return jsonify({"message": "Firma başarıyla güncellendi", "firm": firm}), 200
    return jsonify({"error": "Firma bulunamadı"}), 404

@app.route('/firms/<int:id>', methods=['DELETE'])
def delete_firm(id):
    """Firmayı siler."""
    global firms
    firms = [firm for firm in firms if firm['id'] != id]
    return jsonify({"message": "Firma başarıyla silindi"}), 200

# Varsayılan port, Render tarafından sağlanan $PORT değerinden alınır.
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)


