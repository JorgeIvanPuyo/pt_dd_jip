import React from "react";
import {
  Box,
  Typography,
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TableRow,
  Paper,
} from "@mui/material";

const RouteInfo = ({ routeData }) => {
  if (!routeData) {
    return null;
  }

  const { id, conductor, fecha_programada, notas, ordenes, source } = routeData;

  console.log("data en RouteInfo:", routeData);
  return (
    <Box sx={{ marginTop: "16px" }}>
      <Typography variant="h6" gutterBottom>
        Información de la Ruta
      </Typography>
      <Box>
        <Typography>
          <strong>ID:</strong> {id}
        </Typography>
        <Typography>
          <strong>Conductor:</strong> {conductor?.nombre || "N/A"}
        </Typography>
        <Typography>
          <strong>Fecha Programada:</strong> {fecha_programada || "N/A"}
        </Typography>
        <Typography>
          <strong>Notas:</strong> {notas || "N/A"}
        </Typography>
        <Typography>
          <strong>Fuente:</strong> {source || "N/A"}
        </Typography>
      </Box>

      {ordenes && ordenes.length > 0 && (
        <TableContainer component={Paper} sx={{ marginTop: "16px" }}>
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
              {ordenes.map((orden, index) => (
                <TableRow key={orden.id}>
                  <TableCell>{index + 1}</TableCell>
                  <TableCell>{orden.id}</TableCell>
                  <TableCell>{orden.valor || "N/A"}</TableCell>
                  <TableCell>{orden.prioridad ? "Sí" : "No"}</TableCell>
                </TableRow>
              ))}
            </TableBody>
          </Table>
        </TableContainer>
      )}
    </Box>
  );
};

export default RouteInfo;
