from flask import Flask, request, jsonify
from flask_cors import CORS
from controllers.results_controller import get_results

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def home():
    query = request.args.get('query', '')
    return get_results(query)

if __name__ == '__main__':
    app.run(debug=True)