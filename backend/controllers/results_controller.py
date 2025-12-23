from models.searches_model import Amazon_searches, MercadoLivre_searches
from flask import jsonify

def get_amazon_results(query):
    amazon_search = Amazon_searches(query)
    results = amazon_search.perform_search()
    return jsonify(results)

def get_mercado_results(query):
    mercado_search = MercadoLivre_searches(query)
    results = mercado_search.perform_search()
    return jsonify(results)