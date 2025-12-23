import { useState } from "react";
import { useNavigate } from "react-router-dom"

function Home() {
    const navigate = useNavigate();
    const [searchQuery, setSearchQuery] = useState("");

    function handleSearch() {
        navigate('/search/' + searchQuery);
    }

    return (
      <div className="home-container">
        <h1 className="home-title">Preçometro</h1>
        <p className="home-description">Comparação de preços em diferentes lojas online.</p>
        <h3 className="home-subtitle">Comece com uma busca:</h3>
        <div className="search-bar">
          <input className="search-input" value={searchQuery} type="text" placeholder="Digite o produto..."
          onChange={(e) => setSearchQuery(e.target.value)}
          />
          <button onClick={handleSearch} className="search-button">Buscar</button>
        </div>
      </div>
    )
  }
  
  export default Home
