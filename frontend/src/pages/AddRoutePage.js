import React, { useState } from 'react';
import RouteForm from '../components/RouteForm';
import api from '../api/api';

const AddRoutePage = () => {
  const [routeData, setRouteData] = useState({
    id: '',
    conductor: '',
    fecha: '',
    notas: '',
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setRouteData({ ...routeData, [name]: value });
  };

  const  handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await api.post('/rutas', routeData); 
      alert('Ruta guardada correctamente');
    } catch (error) {
      console.error('Error al guardar la ruta:', error);
      alert('Ocurrió un error al guardar la ruta.');
    }
  };

  return (
    <div>
      <h1>Añadir Ruta</h1>
      <RouteForm
        routeData={routeData}
        onChange={handleChange}
        onSubmit={handleSubmit}
        isEdit={false} // No es modo edición
      />
    </div>
  );
};

export default AddRoutePage;
