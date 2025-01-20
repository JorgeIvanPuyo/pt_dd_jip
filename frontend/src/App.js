import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import RoutesPage from './pages/RoutesPage';
import AddRoutePage from './pages/AddRoutePage';
import RouteDetailsPage from './pages/RouteDetailsPage';
import SearchRoutePage from './pages/SearchRoutePage';

function App() {
  return (
    <Router>
      <header style={{ width: "100%",
          background: "white", 
          position: "fixed", 
          top: 0,
          zIndex: 1000, }}>
        <img
          src="/images/banner.webp"
          alt="Banner"
          style={{
            width: "100%",
            height: "160px",
            objectFit: "cover"
          }}
        />
      </header>
      <div style={{ marginTop: "160px" }}>
        <Routes>
          <Route path="/" element={<RoutesPage />} />
          <Route path="/add-route" element={<AddRoutePage />} />
          <Route path="/route-details/:id" element={<RouteDetailsPage />} />
          <Route path="/search-route" element={<SearchRoutePage />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
