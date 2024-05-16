from flask import Flask, request, jsonify, render_template
from kubernetes import client, config

app = Flask(__name__)

# Load Kubernetes configuration
config.load_kube_config()

v1 = client.CoreV1Api()
apps_v1 = client.AppsV1Api()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/deploy', methods=['POST'])
def deploy():
    namespace = request.form.get('namespace')
    app_name = request.form.get('app_name')
    # Add logic to deploy application using Helm
    return jsonify({"status": "Deployment initiated"})

@app.route('/destroy', methods=['POST'])
def destroy():
    namespace = request.form.get('namespace')
    app_name = request.form.get('app_name')
    # Add logic to destroy application using Helm
    return jsonify({"status": "Destruction initiated"})

@app.route('/status', methods=['GET'])
def status():
    namespace = request.args.get('namespace')
    pods = v1.list_namespaced_pod(namespace)
    pod_statuses = [{"name": pod.metadata.name, "status": pod.status.phase} for pod in pods.items]
    return jsonify(pod_statuses)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
