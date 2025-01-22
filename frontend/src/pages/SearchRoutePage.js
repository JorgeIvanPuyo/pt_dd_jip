import React, { useState } from "react";
import {
  Box,
  Button,
  TextField,
  Typography,
  Alert,
} from "@mui/material";
import api from "../api/api";
import RouteInfo from "../components/RouteInfo";

const SearchRoutePage = () => {
  const [routeData, setRouteData] = useState(null);
  const [routeId, setRouteId] = useState("");
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  const handleSearch = async () => {
    if (!routeId) {
      setError("Por favor ingrese un ID de ruta válido.");
      return;
    }

    setLoading(true);
    setError("");

    try {
      const response = await api.get(`/fetch/${routeId}`);
      setRouteData(response.data); 
    } catch (error) {
      console.error("Error al buscar la ruta:", error);
      setError("La ruta no fue encontrada en la base de datos ni en el servicio externo.");
      setRouteData(null);
    } finally {
      setLoading(false);
    }
  };

  return (
    <Box sx={{ padding: "16px", maxWidth: "600px", margin: "0 auto" }}>
      <Typography variant="h4" gutterBottom textAlign="center">
        Consultar Ruta
      </Typography>

      <TextField
        label="ID de la Ruta"
        name="routeId"
        value={routeId}
        onChange={(e) => setRouteId(e.target.value)}
        fullWidth
        sx={{ marginBottom: "16px" }}
      />

      {error && (
        <Alert severity="error" sx={{ marginBottom: "16px" }}>
          {error}
        </Alert>
      )}

      <Button
        variant="contained"
        color="primary"
        onClick={handleSearch}
        disabled={loading}
        fullWidth
      >
        {loading ? "Buscando..." : "Buscar Ruta"}
      </Button>

      {routeData && <RouteInfo routeData={routeData} />}
    </Box>
  );
};

export default SearchRoutePage;