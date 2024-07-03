import os
from flask import Flask, jsonify, render_template
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/estrai', methods=['GET'])
def estrai_superenalotto():
    numeri = list(range(1, 91))
    estratti = random.sample(numeri, 6)
    estratti.sort()
    numeri_rimanenti = [n for n in numeri if n not in estratti]
    numero_jolly = random.choice(numeri_rimanenti)
    numero_superstar = random.choice(numeri)
    return jsonify({
        'numeri_estratti': estratti,
        'numero_jolly': numero_jolly,
        'numero_superstar': numero_superstar
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)

