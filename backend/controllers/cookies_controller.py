from flask import jsonify, make_response, request
import json

def set_data_cookie(search_name, search_data):
    cookie_name = search_name.upper().replace(" ", "_").strip()
    response = make_response(jsonify({"message": f"{search_name} data stored in cookie"}))
    response.set_cookie(cookie_name, value=json.dumps(search_data), max_age=60*60*48) # Validade de 2 dias 
    return response

def get_data_cookie(search_name):
    cookie_name = search_name.upper().replace(" ", "_").strip()
    cookie_data = request.cookies.get(cookie_name)
    if cookie_data:
        return jsonify(cookie_data)
    else:
        return None