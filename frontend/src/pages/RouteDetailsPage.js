import React, { useState, useEffect } from "react";
import { useParams, useLocation, useNavigate } from "react-router-dom";
import RouteFullForm from "../components/RouteFullForm";
import api from "../api/api";
import { Typography, Box } from "@mui/material";

const RouteDetailsPage = () => {
  const { id } = useParams();
  const location = useLocation();
  const navigate = useNavigate();
  const [routeData, setRouteData] = useState(
    location.state?.routeData || {
      id: "",
      conductor: null,
      fecha_programada: "",
      notas: "",
      ordenes: [],
    }
  );
  const [isLoading, setIsLoading] = useState(!location.state?.routeData);

  useEffect(() => {
    const fetchRoute = async () => {
      if (location.state?.routeData) return; 
      try {
        const response = await api.get(`/rutas/${id}/ordenes`);
        setRouteData({
          id: response.data.id,
          conductor: response.data.conductor,
          fecha_programada: response.data.fecha_programada,
          notas: response.data.notas,
          ordenes: response.data.ordenes,
        });
        setIsLoading(false);
      } catch (error) {
        console.error("Error al obtener la ruta:", error);
        alert("Ocurrió un error al cargar los datos de la ruta.");
      }
    };

    fetchRoute();
  }, [id, location.state?.routeData]);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setRouteData((prevData) => ({ ...prevData, [name]: value }));
  };

  const handleSave = async () => {
    try {
      await api.put(`/rutas/${id}`, routeData);
      alert("Ruta actualizada correctamente");
      navigate("/"); 
    } catch (error) {
      console.error("Error al actualizar la ruta:", error);
      alert("Ocurrió un error al actualizar la ruta.");
    }
  };

  if (isLoading) {
    return <Typography>Cargando...</Typography>;
  }

  return (
    <Box sx={{ padding: "16px" }}>
      <Typography variant="h4" gutterBottom sx={{ textAlign: "center" }}>
        Detalles de la Ruta
      </Typography>

      <RouteFullForm
        routeData={routeData}
        onChange={handleChange}
        onSave={handleSave}
        isEdit={true}
      />
    </Box>
  );
};

export default RouteDetailsPage;
