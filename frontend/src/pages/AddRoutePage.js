import React, { useState } from "react";
import { Box, Button, TextField, Typography, Alert } from "@mui/material";
import RouteFullForm from "../components/RouteFullForm";
import api from "../api/api";

const AddRoutePage = () => {
  const [routeData, setRouteData] = useState({
    id: "",
    conductor: "",
    fecha_programada: "",
    notas: "",
    ordenes: [],
  });
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);
  const [isRouteFound, setIsRouteFound] = useState(false);
  const [routeSource, setRouteSource] = useState(null); 

  const handleSearch = async () => {
    if (!routeData.id) {
      setError("Por favor ingrese un ID de ruta válido.");
      return;
    }

    setLoading(true);
    setError("");

    try {
      const response = await api.get(`/fetch/${routeData.id}`);
      if (response.data) {
        setRouteData({
          id: response.data.id,
          conductor: response.data.conductor,
          fecha_programada: response.data.fecha_programada || "",
          notas: response.data.notas || "",
          ordenes: response.data.ordenes || [],
        });
        setIsRouteFound(true);
        if (response.data.source === "db") {
          setRouteSource("db");
        } else if (response.data.source === "external") {
          setRouteSource("external");
        }
      }
    } catch (error) {
      console.error("Error al buscar la ruta:", error);
      setError(
        "La ruta no fue encontrada en la base de datos ni en el servicio externo."
      );
      setRouteData({
        id: routeData.id, 
        conductor: "",
        fecha_programada: "",
        notas: "",
        ordenes: [],
      });
      setIsRouteFound(false);
    } finally {
      setLoading(false);
    }
  };

  const handleReset = () => {
    setRouteData({
      id: "",
      conductor: "",
      fecha_programada: "",
      notas: "",
      ordenes: [],
    });
    setError("");
    setIsRouteFound(false);
  };

  const handleSave = async () => {
    try {
      if (routeSource === "db") {
        await api.put(`/rutas/${routeData.id}`, routeData);
        alert("Ruta actualizada correctamente.");
      } else if (routeSource === "external") {
        await api.post("/rutas/", routeData);
        alert("Ruta creada correctamente.");
      } else {
        throw new Error("No se puede determinar el origen de la ruta.");
      }
      handleReset();
    } catch (error) {
      console.error("Error al guardar la ruta:", error);
      alert("Ocurrió un error al guardar la ruta.");
    }
  };

  return (
    <Box sx={{ padding: "16px", maxWidth: "800px", margin: "0 auto" }}>
      <Typography variant="h4" gutterBottom textAlign="center">
        Buscar y Añadir Ruta
      </Typography>

      <TextField
        label="ID de la Ruta"
        name="id"
        value={routeData.id}
        onChange={(e) =>
          setRouteData({
            ...routeData,
            id: e.target.value,
            conductor: "",
            fecha_programada: "",
            notas: "",
            ordenes: [],
          })
        }
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
        sx={{ marginBottom: "16px" }}
      >
        {loading ? "Buscando..." : "Buscar Ruta"}
      </Button>

      {isRouteFound && (
        <RouteFullForm
          routeData={routeData}
          onChange={(e) => {
            const { name, value } = e.target;
            setRouteData({ ...routeData, [name]: value });
          }}
          onSave={handleSave}
          isEdit={isRouteFound}
        />
      )}
    </Box>
  );
};

export default AddRoutePage;
