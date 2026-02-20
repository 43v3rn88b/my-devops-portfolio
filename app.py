from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Hello from the DevSecOps Pipeline!", "status": "success"})

@app.route('/health')
def health():
    # This endpoint is used by Docker and Kubernetes to check if the app is alive
    return jsonify({"status": "up", "checks": "all passed"}), 200

if __name__ == '__main__':
    # Listens on all interfaces (0.0.0.0) so Docker can expose it
    app.run(host='0.0.0.0', port=5000)