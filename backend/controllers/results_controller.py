from models.searches_model import Amazon_searches, MercadoLivre_searches, Ebay_searches
from flask import jsonify
from controllers.cookies_controller import set_data_cookie, get_data_cookie

def get_amazon_results(query):
    amazon_search = Amazon_searches(query)
    results = amazon_search.perform_search()
    return jsonify(results)

def get_mercado_results(query):
    mercado_search = MercadoLivre_searches(query)
    results = mercado_search.perform_search()
    return jsonify(results)

def get_ebay_results(query):
    ebay_search = Ebay_searches(query)
    results = ebay_search.perform_search()
    return jsonify(results)

def get_results(query):
    existing_data = get_data_cookie("combined_results")
    if existing_data:
        return existing_data
    amazon_results = get_amazon_results(query).json if hasattr(get_amazon_results(query), 'json') else []
    mercado_results = get_mercado_results(query).json if hasattr(get_mercado_results(query), 'json') else []
    ebay_results = get_ebay_results(query).json if hasattr(get_ebay_results(query), 'json') else []
    combined_results = amazon_results + mercado_results + ebay_results
    set_data_cookie(query, combined_results)
    return jsonify(combined_results)
