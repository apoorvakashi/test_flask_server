from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, World!"

if __name__ == "__main__":
    # Run on all available IP addresses (0.0.0.0) and specify the port
    app.run(debug=True, host='0.0.0.0', port=5000)
