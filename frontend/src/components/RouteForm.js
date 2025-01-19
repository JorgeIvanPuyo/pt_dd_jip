import React, { useState, useEffect } from 'react';
import api from '../api/api';

const RouteForm = ({ routeData, onChange, onSubmit, isEdit }) => {
  const [conductores, setConductores] = useState([]);

  useEffect(() => {
    const fetchConductores = async () => {
      try {
        const response = await api.get('/conductores');
        setConductores(response.data);
      } catch (error) {
        console.error('Error al obtener los conductores:', error);
        alert('No se pudieron cargar los conductores.');
      }
    };

    fetchConductores();
  }, []);

  return (
    <form onSubmit={onSubmit}>
      <div>
        <label htmlFor="id">ID Ruta</label>
        <input
          type="text"
          id="id"
          name="id"
          value={routeData.id}
          onChange={onChange}
          disabled={isEdit} 
        />
      </div>
      <div>
        <label htmlFor="conductor">Conductor</label>
        <select
          id="conductor"
          name="conductor"
          value={routeData.conductor}
          onChange={onChange}
        >
          <option value="" disabled>
            Seleccione un conductor
          </option>
          {conductores.map((conductor) => (
            <option key={conductor.id} value={conductor.id}>
              {conductor.nombre}
            </option>
          ))}
        </select>
      </div>
      <div>
        <label htmlFor="fecha">Fecha Programada</label>
        <input
          type="date"
          id="fecha"
          name="fecha"
          value={routeData.fecha}
          onChange={onChange}
        />
      </div>
      <div>
        <label htmlFor="notas">Notas</label>
        <textarea
          id="notas"
          name="notas"
          value={routeData.notas}
          onChange={onChange}
        />
      </div>
      <button type="submit">Guardar</button>
    </form>
  );
};

export default RouteForm;
