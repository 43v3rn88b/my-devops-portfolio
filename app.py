from flask import Flask, jsonify
import time # Add this import
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
# Set up Prometheus metrics

metrics = PrometheusMetrics(app)
# Optional: Add static information to your metrics
metrics.info('app_info', 'Application info', version='1.0.0')

@app.route('/resume')
def resume():
    import time
    # This is the trap! It makes the test wait 2 seconds.
    time.sleep(2) 
    return '{"message": "Welcome to my DevSecOps Resume API"}'

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

