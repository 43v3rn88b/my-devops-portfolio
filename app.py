from flask import Flask, jsonify
import time # Add this import

app = Flask(__name__)

@app.route('/')
def home():
    time.sleep(2) # Sleep for 2 seconds (2000ms)
    return jsonify({"message": "Hello from the DevSecOps Pipeline!", "status": "success"})

@app.route('/health')
def health():
    # This endpoint is used by Docker and Kubernetes to check if the app is alive
    return jsonify({"status": "up", "checks": "all passed"}), 200

if __name__ == '__main__':
    # Listens on all interfaces (0.0.0.0) so Docker can expose it

    app.run(host='0.0.0.0', port=5000)
