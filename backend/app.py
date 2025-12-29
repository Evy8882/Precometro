from flask import Flask, request, jsonify, make_response
from flask_cors import CORS
from controllers.results_controller import get_results

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def home():
    query = request.args.get('query', '')
    sort_type = request.args.get('sort', '')
    single_store = request.args.get('store', '')
    results = get_results(query, sort_type, single_store)
    if results:
        response = make_response(results, 200)
        return response
    return make_response(jsonify({"error": "Parametros de busca inválidos", "status": 401, "success": False }), 401)

if __name__ == '__main__':
    app.run(debug=True)