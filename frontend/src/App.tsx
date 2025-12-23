import './App.css';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Home from './pages/home';
import Search from './pages/Search';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path='/search/:query' element={<Search />} />
      </Routes>
    </Router>
  );
}

export default App;
