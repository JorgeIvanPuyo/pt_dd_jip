import React, { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import api from "../api/api";
import {
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TableRow,
  Paper,
  Button,
  Typography,
  Box,
  IconButton,
} from "@mui/material";
import DeleteIcon from "@mui/icons-material/Delete";
import VisibilityIcon from "@mui/icons-material/Visibility";

const RoutesPage = () => {
  const [routes, setRoutes] = useState([]);

  const fetchRoutes = async () => {
    try {
      const response = await api.get("/rutas");
      setRoutes(response.data);
    } catch (error) {
      console.error("Error al obtener las rutas:", error);
      alert("Ocurrió un error al cargar las rutas.");
    }
  };

  const handleDelete = async (id) => {
    if (window.confirm("¿Está seguro de que desea eliminar esta ruta?")) {
      try {
        await api.delete(`/rutas/${id}`);
        alert("Ruta eliminada correctamente");
        setRoutes((prevRoutes) =>
          prevRoutes.filter((route) => route.id !== id)
        );
      } catch (error) {
        console.error("Error al eliminar la ruta:", error);
        alert("Ocurrió un error al eliminar la ruta.");
      }
    }
  };

  useEffect(() => {
    fetchRoutes();
  }, []);

  return (
    <Box sx={{ padding: "16px", maxWidth: "800px", margin: "0 auto" }}>
      <Typography variant="h4" gutterBottom sx={{ textAlign: "center" }}>
        Lista de Rutas
      </Typography>
      <Box
        sx={{
          display: "flex",
          justifyContent: "flex-end",
          marginTop: "16px",
          gap: "16px",
        }}
      >
        <Link to="/add-route">
          <Button variant="contained" color="secondary">
          Añadir Ruta
          </Button>
        </Link>
        <Link to="/search-route">
          <Button variant="contained" color="secondary">
          Consultar Ruta
          </Button>
        </Link>
      </Box>
      {routes.length === 0 ? (
        <Typography
          variant="body1"
          sx={{ marginTop: "16px", textAlign: "center" }}
        >
          No hay rutas disponibles para mostrar.
        </Typography>
      ) : (
        <TableContainer
          component={Paper}
          sx={{ boxShadow: 3, borderRadius: "8px" }}
        >
          <Table>
            <TableHead>
              <TableRow>
                <TableCell>#</TableCell>
                <TableCell>Ruta</TableCell>
                <TableCell>Conductor</TableCell>
                <TableCell>Fecha</TableCell>
                <TableCell>Acciones</TableCell>
              </TableRow>
            </TableHead>
            <TableBody>
              {routes.map((route, index) => (
                <TableRow key={route.id}>
                  <TableCell>{index + 1}</TableCell>
                  <TableCell>{route.id}</TableCell>
                  <TableCell>{route.conductor}</TableCell>
                  <TableCell>{route.fecha_programada}</TableCell>
                  <TableCell>
                    <Box
                      sx={{
                        display: "flex",
                        gap: "16px",
                        alignItems: "center",
                      }}
                    >
                      <IconButton
                        color="primary"
                        component={Link}
                        to={`/route-details/${route.id}`}
                        aria-label="Ver detalles"
                      >
                        <VisibilityIcon />
                      </IconButton>
                      <IconButton
                        color="error"
                        onClick={() => handleDelete(route.id)}
                        aria-label="Eliminar"
                      >
                        <DeleteIcon />
                      </IconButton>
                    </Box>
                  </TableCell>
                </TableRow>
              ))}
            </TableBody>
          </Table>
        </TableContainer>
      )}
    </Box>
  );
};

export default RoutesPage;
