from flask import Flask, request, jsonify
from controllers.results_controller import get_amazon_results, get_mercado_results

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    query = request.args.get('query', '')
    return get_mercado_results(query)

if __name__ == '__main__':
    app.run(debug=True)