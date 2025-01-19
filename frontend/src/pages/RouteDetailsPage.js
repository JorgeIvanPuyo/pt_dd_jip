import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import RouteForm from '../components/RouteForm';
import api from '../api/api';

const RouteDetailsPage = () => {
  const { id } = useParams();
  const [routeData, setRouteData] = useState({
    id: '',
    conductor: '',
    fecha: '',
    notas: '',
    ordenes: [], 
  });

  useEffect(() => {
    const fetchRoute = async () => {
      try {
        const response = await api.get(`/rutas/${id}/ordenes`); 
        setRouteData({
          id: response.data.id,
          conductor: response.data.conductor,
          fecha: response.data.fecha_programada,
          notas: response.data.notas,
          ordenes: response.data.ordenes, 
        });
        console.log("Rutas:", response.data);
      } catch (error) {
        console.error('Error al obtener la ruta:', error);
        alert('Ocurrió un error al cargar los datos de la ruta.');
      }
    };

    fetchRoute();
  }, [id]);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setRouteData({ ...routeData, [name]: value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await api.put(`/rutas/${id}`, routeData); 
      alert('Ruta actualizada correctamente');
    } catch (error) {
      console.error('Error al actualizar la ruta:', error);
      alert('Ocurrió un error al actualizar la ruta.');
    }
  };

  return (
    <div>
      <h1>Detalles de la Ruta</h1>
      <RouteForm
        routeData={routeData}
        onChange={handleChange}
        onSubmit={handleSubmit}
        isEdit={true} 
      />

      {/* Tabla para mostrar las órdenes */}
      <h2>Órdenes Asociadas</h2>
      <table>
        <thead>
          <tr>
            <th>Orden</th>
            <th>Valor</th>
            <th>Prioritario</th>
          </tr>
        </thead>
        <tbody>
          {routeData.ordenes.map((orden, index) => (
            <tr key={orden.id}>
              <td>{orden.id}</td>
              <td>{orden.valor || 'N/A'}</td>
              <td>
                <input
                  type="checkbox"
                  disabled
                  checked={orden.prioridad || false}
                  readOnly
                />
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default RouteDetailsPage;
