import { useState, useEffect } from "react";
import { useNavigate, useParams } from "react-router-dom"

function Search() {
    const navigate = useNavigate();
    const { query, index } = useParams<{ query: string; index?: string }>();
    const searchParams = new URLSearchParams(window.location.search);
    const single_store = searchParams.get('single_store') || "";
    const sort = searchParams.get('sort') || "";
    const currentIndex = index ? parseInt(index) : 0;
    const [searchQuery, setSearchQuery] = useState(query || "");
    const [searchSingleStore, setSearchSingleStore] = useState(single_store || "");
    const [searchSortType, setSearchSortType] = useState(sort || "");
    const [loading, setLoading] = useState(true);
    const [searchErr, setSearchErr] = useState(false);
    const api_url = import.meta.env.VITE_API_URL || 'http://localhost:5000'

    type Product = {
        title: string,
        price: string,
        image: string,
        rating: string,
        engine: string,
        link: string
    }

    const [products, setProducts] = useState<Product[]>([]);

    useEffect(() => {
        setLoading(true);
        setSearchErr(false);
        
        const params = new URLSearchParams();
        params.append('query', query || '');
        if (single_store) params.append('store', single_store);
        if (sort) params.append('sort', sort);
        
        fetch(api_url + '/?' + params.toString())
        .then(res => res.json())
            .then(body => {
                if (!body.success) {
                    if (body.status === 401) {
                        setLoading(false);
                        setSearchErr(true);
                        throw new Error('Invalid search parameters');
                    }
                }
                return body.data;
            })
            .then(data => {
                const fetchedProducts = data[currentIndex].map((item: any) => ({
                    title: item.title,
                    price: item.price,
                    image: item.image,
                    link: item.link,
                    rating: item.rating,
                    engine: item.engine
                }));
                setProducts(fetchedProducts);
                setLoading(false);
            }).catch(err => {
                console.error('Error fetching products:', err);
                setLoading(false);
            });
    }, [query, currentIndex, api_url, single_store, sort]);

    function handleSearch() {
        const params = new URLSearchParams();
        if (searchSingleStore) params.append('single_store', searchSingleStore);
        if (searchSortType) params.append('sort', searchSortType);
        navigate('/search/' + searchQuery + (params.toString() ? '?' + params.toString() : ''));
    }

    return (
      <div className="search-container">
        <header className="search-header">
            <h1 className="home-title">Preçometro</h1>
            <form className="search-bar">
            <input className="search-input" value={searchQuery} type="text" placeholder="Digite o produto..."
            onChange={(e) => setSearchQuery(e.target.value)}
            />
            <select name="single_store" value={searchSingleStore} onChange={(e) => setSearchSingleStore(e.target.value)}>
                <option value="">Todas as lojas</option>
                <option value="amazon">Apenas Amazon</option>
                <option value="mercadolivre">Apenas Mercado Livre</option>
                <option value="ebay">Apenas eBay</option>
            </select>
            <select name="sort" value={searchSortType} onChange={(e) => setSearchSortType(e.target.value)}>
                <option value="">Ordenação aleatória</option>
                <option value="price_low_to_high">Preço: Menor para Maior</option>
                <option value="price_high_to_low">Preço: Maior para Menor</option>
                <option value="rating_high_to_low">Avaliação: Maior para Menor</option>
            </select>
            <button onClick={handleSearch} className="search-button">Buscar</button>
            </form>
        </header>
        <div className="results-container">
            {loading ? (
                <p>Carregando resultados...</p>
            ) : (
                products.length === 0 ? (
                    <p>Nenhum resultado encontrado para "{query}".</p>
                ) : (
                    searchErr ? (<p>Parametros de busca inválidos...</p>) : (
                    products.map((product, index) => (
                        <div key={index} className="product-card">
                            <img src={product.image} alt={product.title} className="product-image" />
                            <h2 className="product-title">{product.title}</h2>
                            <p className="product-price">Preço: {product.price}</p>
                            <p className="product-rating">Avaliação: {product.rating}</p>
                            <a href={product.link} className="product-link" target="_blank" rel="noopener noreferrer">Visitar {product.engine}</a>
                        </div>
                        )
                    ))
                )
            )}
        </div>
      </div>
    )
}
  
  export default Search
