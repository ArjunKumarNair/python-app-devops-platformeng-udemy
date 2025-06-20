from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/v1/details')
def details():
    return jsonify({
        'message': 'Hello World',
    })

@app.route('/api/v1/healthz')
def health():
    return jsonify({
        'status': 'up',
    }), 200

if __name__ == '__main__':
    app.run(host="0.0.0.0")