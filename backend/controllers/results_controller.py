from models.searches_model import Amazon_searches, MercadoLivre_searches, Ebay_searches
from flask import jsonify
from controllers.cookies_controller import set_data_cookie, get_data_cookie
import random

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

def sort_results(results, type):
    if type == "price_low_to_high":
        return sorted(results, key=lambda x: float(x['price'].replace('$', '').replace(',', '').strip()) if x['price'] not in ['No price found', ''] else float('inf'))
    elif type == "price_high_to_low":
        return sorted(results, key=lambda x: float(x['price'].replace('$', '').replace(',', '').strip()) if x['price'] not in ['No price found', ''] else float('-inf'), reverse=True)
    elif type == "rating_high_to_low":
        return sorted(results, key=lambda x: float(x['rating'].split()[0]) if x['rating'] not in ['No rating found', ''] else float('-inf'), reverse=True)
    else:
        return results


def split_list(input_list, chunk_size) -> list:
    splitted_list = []
    for i in range(0, len(input_list), chunk_size):
        splitted_list.append(input_list[i:i + chunk_size])
    return splitted_list 

def get_results(query, sort_type, single_store):
    if not query:
        return None
    
    amazon_results = []
    mercado_results = []
    ebay_results = []
    if not single_store:
        amazon_results = get_amazon_results(query).json if hasattr(get_amazon_results(query), 'json') else []
        mercado_results = get_mercado_results(query).json if hasattr(get_mercado_results(query), 'json') else []
        ebay_results = get_ebay_results(query).json if hasattr(get_ebay_results(query), 'json') else []
    else:
        if single_store.lower() == "amazon":
            amazon_results = get_amazon_results(query).json if hasattr(get_amazon_results(query), 'json') else []
        elif single_store.lower() == "mercadolivre":
            mercado_results = get_mercado_results(query).json if hasattr(get_mercado_results(query), 'json') else []
        elif single_store.lower() == "ebay":
            ebay_results = get_ebay_results(query).json if hasattr(get_ebay_results(query), 'json') else []
        else:
            return None
        
    
    combined_results = amazon_results + mercado_results + ebay_results

    if (sort_type):
        combined_results = sort_results(combined_results, sort_type)
    else:
        random.shuffle(combined_results)

    splitted_results = split_list(combined_results, 15)
    
    return jsonify({"data": splitted_results, "status": 200, "success": True, "results": len(combined_results)})
