from flask import Flask

from flask import jsonify

app = Flask(__name__)

@app.route('/')

def home():
    return "hello this is aditya am learning cicd version one more 11.0"

@app.route('/health')
def health():
    return jsonify({"status": "healthy"})

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000,debug=True)