import requests
from controllers.cookies_controller import get_data_cookie, set_data_cookie
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import os

load_dotenv()

class Searches:
    def __init__(self, query):
        self.query = query
    

class Amazon_searches(Searches):
    def __init__(self, query):
        super().__init__(query)
    def perform_search(self):

        existing_data = get_data_cookie(f"amazon_{self.query}".upper())
        if existing_data:
            return existing_data

        # Gerar chave API em https://serpapi.com/
        # Usos mensais do plano gratuito: 250
        api_key = os.getenv("API_KEY")
        params = {
            "api_key": api_key,
            "engine": "amazon",
            "k": self.query,
            "amazon_domain": "amazon.com",
        }
        search = requests.get(f"https://serpapi.com/search.json", params=params)
        response = search.json()
        results = []
        for i, result in enumerate(response.get("organic_results", [])):
            if i >= 12:
                break
            title = result.get("title", "No title found")
            price = result.get("price", "No price found")
            image = result.get("thumbnail", "")
            rating = result.get("rating", "No rating found")
            link = result.get("link", "")
            results.append({"engine": "amazon","title": title, "price": price, "image": image, "rating": rating, "link": link})
        set_data_cookie(f"amazon_{self.query}".upper(), results)
        return results
        # all_items = page_data.find_all("div", class_="sg-col-inner")
        # results = []
        # for item in all_items:
        #     price = item.find("span", class_="a-price").text
        #     title = item.find("h2")
        #     title_span = title.find("span").text if title else "No title found"
        #     results.append({"title": title_span, "price": price})
        # return results
        
class MercadoLivre_searches(Searches):
    def __init__(self,query):
        super().__init__(query)
    def perform_search(self):

        existing_data = get_data_cookie(f"mercadolivre_{self.query}".upper())
        if existing_data:
            return existing_data

        search_url = f"https://lista.mercadolivre.com.br/{self.query.replace(' ', '-')}"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
        }
        response = requests.get(search_url, headers=headers)
        soup = BeautifulSoup(response.content, "html.parser")
        all_items = soup.find_all("li", class_="ui-search-layout__item")
        results = []
        for i, item in enumerate(all_items):
            if i >= 12:
                break
            title = item.find("a", class_="poly-component__title").text
            price = item.find("span", class_="andes-money-amount__fraction").text
            image = item.find("img", class_="poly-component__picture")["src"]
            rating = item.find("span", class_="poly-phrase-label").text if item.find("span", class_="poly-phrase-label") else "No rating found",
            link = item.find("a", class_="poly-component__title")["href"]
            results.append({"engine": "mercadolivre","title": title, "price": price, "image": image, "rating": rating, "link": link})
        set_data_cookie(f"mercadolivre_{self.query}".upper(), results)
        return results
            
class Ebay_searches(Searches):
    def __init__(self, query):
        super().__init__(query)
    def perform_search(self):
        existing_data = get_data_cookie(f"ebay_{self.query}".upper())
        if existing_data:
            return existing_data
        # Gerar chave API em https://serpapi.com/
        # Usos mensais do plano gratuito: 250
        api_key = os.getenv("API_KEY")
        params = {
            "api_key": api_key,
            "engine": "ebay",
            "_nkw": self.query,
            "ebay_domain": "ebay.com",
        }
        search = requests.get(f"https://serpapi.com/search.json", params=params)
        response = search.json()
        results = []
        for i, result in enumerate(response.get("organic_results", [])):
            if i >= 12:
                break
            title = result.get("title", "No title found")
            price_raw = result.get("price", {"raw": "No price found"})
            price = ""
            if "to" in price_raw:
                price = price_raw["to"]["raw"]
            else:
                price = price_raw["raw"]
            image = result.get("thumbnail", "")
            rating = result.get("rating", "No rating found")
            link = result.get("link", "")
            results.append({"engine": "ebay","title": title, "price": price, "image": image, "rating": rating, "link": link})
        
        set_data_cookie(f"ebay_{self.query}".upper(), results)
        return results