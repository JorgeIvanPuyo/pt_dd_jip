import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import api from '../api/api';

const RoutesPage = () => {
  const [routes, setRoutes] = useState([]);

  const fetchRoutes = async () => {
    try {
      const response = await api.get('/rutas'); 
      setRoutes(response.data); 
    } catch (error) {
      console.error('Error al obtener las rutas:', error);
      alert('Ocurrió un error al cargar las rutas.');
    }
  };

  useEffect(() => {
    fetchRoutes();
  }, []);

  return (
    <div>
      <h1>Lista de Rutas</h1>
      <table border="1">
        <thead>
          <tr>
            <th>Ruta</th>
            <th>Conductor</th>
            <th>Fecha</th>
            <th>Acciones</th>
          </tr>
        </thead>
        <tbody>
          {routes.map(route => (
            <tr key={route.id}>
              <td>{route.id}</td>
              <td>{route.conductor}</td>
              <td>{route.fecha_programada}</td>
              <td>
                <Link to={`/route-details/${route.id}`}>Ver</Link>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
      <Link to="/add-route">
        <button>Añadir Ruta</button>
      </Link>
    </div>
  );
};

export default RoutesPage;
