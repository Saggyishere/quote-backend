from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/api/calculate-quote", methods=["POST"])
def calculate_quote():
    return jsonify({
        "price": 12500,
        "scrap_found": True,
        "message": "Use 120kg from inventory"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
