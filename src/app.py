from flask import Flask,jsonify,request,render_template
import socket

app = Flask(__name__)

def fetchdetails():
    try:
        hostname = socket.gethostname()
        host_ip = socket.gethostbyname(hostname)
        return str(hostname),str(host_ip)
    except socket.gaierror as e:
        print(f"Error getting IP address: {e}")
        return "unknown", "unknown"

@app.route("/")
def micro_service():
    return "<p>Welcome to microservice platform</p>"

@app.route('/health')
def health():
    return jsonify(
        status = 'UP'
    )

@app.route('/details')
def details():
    host , ip = fetchdetails()
    return render_template('index.html', HOSTNAME = host , IP = ip)

















if __name__ == "__main__":
    # Set the FLASK_APP environment variable to your app's filename
    # In this case, it's app.py
    import os
    os.environ['FLASK_APP'] = 'app.py'
    
    # Run the Flask app on localhost with default port 5000
    app.run()
