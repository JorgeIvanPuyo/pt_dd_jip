import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import RoutesPage from './pages/RoutesPage';
import AddRoutePage from './pages/AddRoutePage';
import RouteDetailsPage from './pages/RouteDetailsPage';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<RoutesPage />} />
        <Route path="/add-route" element={<AddRoutePage />} />
        <Route path="/route-details/:id" element={<RouteDetailsPage />} />
      </Routes>
    </Router>
  );
}

export default App;
