import { useState } from "react";
import { useNavigate, useParams } from "react-router-dom"

function Search() {
    const navigate = useNavigate();
    const { query, index } = useParams<{ query: string; index?: string }>();
    const currentIndex = index ? parseInt(index) : 0;
    const [searchQuery, setSearchQuery] = useState(query || "");
    const [loading, setLoading] = useState(true);
    const api_url = import.meta.env.VITE_API_URL || 'http://localhost:5000'

    type Product = {
        title: string,
        price: string,
        image: string,
        rating: string,
        engine: string
    }

    const [products, setProducts] = useState<Product[]>([]);

    fetch(api_url + '/?query=' + query)
        .then(res => res.json())
        .then(data => {
            const fetchedProducts = data[currentIndex].map((item: any) => ({
                title: item.title,
                price: item.price,
                image: item.image,
                rating: item.rating,
                engine: item.engine
            }));
            setProducts(fetchedProducts);
            setLoading(false);
        }).catch(err => {
            console.error('Error fetching products:', err);
        });

        function handleSearch() {
            navigate('/search/' + searchQuery);
        }

    return (
      <div className="search-container">
        <header className="search-header">
            <h1 className="home-title">Preçometro</h1>
            <div className="search-bar">
            <input className="search-input" value={searchQuery} type="text" placeholder="Digite o produto..."
            onChange={(e) => setSearchQuery(e.target.value)}
            />
            <button onClick={handleSearch} className="search-button">Buscar</button>
            </div>
        </header>
        <div className="results-container">
            {loading ? (
                <p>Carregando resultados...</p>
            ) : (
                products.length === 0 ? (
                    <p>Nenhum resultado encontrado para "{query}".</p>
                ) : (
                    products.map((product, index) => (
                        <div key={index} className="product-card">
                            <img src={product.image} alt={product.title} className="product-image" />
                            <h2 className="product-title">{product.title}</h2>
                            <p className="product-price">Preço: {product.price}</p>
                            <p className="product-rating">Avaliação: {product.rating}</p>
                            <p className="product-engine">Loja: {product.engine}</p>
                        </div>
                    ))
                )
            )}
        </div>
      </div>
    )
  }
  
  export default Search
