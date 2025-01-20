import React, { useState } from "react";
import {
  Box,
  Button,
  TextField,
  MenuItem,
  Typography,
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TableRow,
  Paper,
  Checkbox,
} from "@mui/material";
import api from "../api/api"; 

const RouteFullForm = ({ routeData, onChange, onSave, isEdit }) => {
  const [conductores, setConductores] = useState([]); 
  const [errors, setErrors] = useState({});
  const [submitError, setSubmitError] = useState("");

  React.useEffect(() => {
    const fetchConductores = async () => {
      try {
        const response = await api.get("/conductores");
        setConductores(response.data);
      } catch (error) {
        console.error("Error al obtener los conductores:", error);
        setSubmitError("No se pudieron cargar los conductores.");
      }
    };

    fetchConductores();
  }, []);

  const validate = () => {
    const newErrors = {};

    if (!routeData.id || isNaN(routeData.id)) {
      newErrors.id = "El ID es requerido y debe ser un número.";
    }
    if (!routeData.conductor || !routeData.conductor.id) {
      newErrors.conductor = "Seleccione un conductor.";
    }
    if (!routeData.fecha_programada) {
      newErrors.fecha_programada = "La fecha programada es requerida.";
    }
    if (!routeData.notas) {
      newErrors.notas = "Las notas son requeridas.";
    }
    if (!routeData.ordenes || routeData.ordenes.length === 0) {
      newErrors.ordenes = "Debe incluir al menos una orden.";
    } else {
      const invalidOrders = routeData.ordenes.filter(
        (orden) => !orden.valor || isNaN(orden.valor)
      );
      if (invalidOrders.length > 0) {
        newErrors.ordenes = "Todas las órdenes deben tener valores numéricos.";
      }
    }

    setErrors(newErrors);
    return Object.keys(newErrors).length === 0;
  };

  const handleSave = (e) => {
    e.preventDefault();
    if (validate()) {
      onSave();
    }
  };

  const totalOrdenes = routeData.ordenes.reduce(
    (total, orden) => total + (orden.valor || 0),
    0
  );

  return (
    <Box
      component="form"
      onSubmit={handleSave}
      sx={{
        display: "flex",
        flexDirection: "column",
        gap: "16px",
        maxWidth: "600px",
        margin: "0 auto",
        padding: "16px",
        boxShadow: 3,
        borderRadius: "8px",
        backgroundColor: "#fff",
      }}
    >
      <Typography variant="h5" textAlign="center">
        {isEdit ? "Editar Ruta" : "Crear Nueva Ruta"}
      </Typography>

      {submitError && <Alert severity="error">{submitError}</Alert>}

      <TextField
        label="ID Ruta"
        id="id"
        name="id"
        value={routeData.id}
        onChange={onChange}
        error={!!errors.id}
        helperText={errors.id}
        fullWidth
        disabled={isEdit}
        InputProps={{
          readOnly: isEdit,
        }}
      />

      <TextField
        select
        label="Conductor"
        name="conductor"
        value={routeData.conductor?.id || ""}
        onChange={(e) => {
          const selectedConductor = conductores.find(
            (c) => c.id === parseInt(e.target.value)
          );
          onChange({ target: { name: "conductor", value: selectedConductor } });
        }}
        error={!!errors.conductor}
        helperText={errors.conductor}
        fullWidth
      >
        <MenuItem value="" disabled>
          Seleccione un conductor
        </MenuItem>
        {conductores.map((conductor) => (
          <MenuItem key={conductor.id} value={conductor.id}>
            {conductor.nombre}
          </MenuItem>
        ))}
      </TextField>

      <TextField
        label="Fecha Programada"
        type="date"
        name="fecha_programada"
        value={routeData.fecha_programada}
        onChange={onChange}
        fullWidth
        error={!!errors.fecha_programada}
        helperText={errors.fecha_programada}
        InputLabelProps={{ shrink: true }}
      />

      <TextField
        label="Notas"
        name="notas"
        value={routeData.notas}
        onChange={onChange}
        fullWidth
        multiline
        rows={4}
        InputLabelProps={{ shrink: true }}
      />
      {errors.notas && (
        <Typography variant="body2" color="error">
          {errors.notas}
        </Typography>
      )}

      <Typography variant="h6" gutterBottom>
        Órdenes Asociadas
      </Typography>
      {errors.ordenes && (
        <Typography variant="body2" color="error" sx={{ marginBottom: "8px" }}>
          {errors.ordenes}
        </Typography>
      )}
      <TableContainer component={Paper}>
        <Table size="small">
          <TableHead>
            <TableRow>
              <TableCell>#</TableCell>
              <TableCell>Orden</TableCell>
              <TableCell>Valor</TableCell>
              <TableCell>Prioritario</TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {routeData.ordenes.map((orden, index) => (
              <TableRow key={orden.id}>
                <TableCell>{index + 1}</TableCell>
                <TableCell>{orden.id}</TableCell>
                <TableCell>
                  <TextField
                    type="number"
                    value={orden.valor}
                    onChange={(e) => {
                      const updatedOrdenes = routeData.ordenes.map((o) =>
                        o.id === orden.id
                          ? { ...o, valor: parseFloat(e.target.value) }
                          : o
                      );
                      onChange({ target: { name: "ordenes", value: updatedOrdenes } });
                    }}
                  />
                </TableCell>
                <TableCell>
                  <Checkbox
                    checked={orden.prioridad}
                    onChange={(e) => {
                      const updatedOrdenes = routeData.ordenes.map((o) =>
                        o.id === orden.id
                          ? { ...o, prioridad: e.target.checked }
                          : o
                      );
                      onChange({ target: { name: "ordenes", value: updatedOrdenes } });
                    }}
                  />
                </TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </TableContainer>

      <Typography variant="body1" sx={{ marginTop: "16px", fontWeight: "bold" }}>
        Total: {totalOrdenes.toFixed(2)} 
      </Typography>

      <Button variant="contained" color="primary" onClick={onSave}>
        Guardar
      </Button>
    </Box>
  );
};

export default RouteFullForm;
