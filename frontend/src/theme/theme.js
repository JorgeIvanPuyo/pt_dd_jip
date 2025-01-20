import { createTheme } from "@mui/material/styles";

const theme = createTheme({
  palette: {
    primary: {
      main: "#132226", 
      light: "#525B56",
      dark: "#132226", 
    },
    secondary: {
      main: "#A4978E",
      light: "#BEA69A", 
      dark: "#7D6E65", 
    },
    text: {
      primary: "#132226", 
      secondary: "#525B56", 
    },
    background: {
      default: "#F5F5F5", 
      paper: "#FFFFFF", 
    },
    error: {
      main: "#BE9063", 
    },
    action: {
      hover: "rgba(0, 0, 0, 0.08)",
    },
  },
  typography: {
    h1: {
      fontSize: "2rem",
      fontWeight: 700,
      color: "#132226", 
    },
    h2: {
      fontSize: "1.5rem",
      fontWeight: 600,
      color: "#525B56", 
    },
    body1: {
      fontSize: "1rem",
      color: "#525B56", 
    },
    button: {
      fontWeight: 600,
      textTransform: "none",
    },
  },
  components: {
    MuiButton: {
      styleOverrides: {
        root: {
          borderRadius: "8px",
          padding: "8px 16px",
        },
        containedPrimary: {
          backgroundColor: "#132226", // Color principal de botones
          color: "#FFFFFF", 
          "&:hover": {
            backgroundColor: "#525B56", 
          },
        },
        containedSecondary: {
          backgroundColor: "#A4978E", // Botones secundarios
          color: "#000000",
          "&:hover": {
            backgroundColor: "#BEA69A", 
          },
        },
        outlinedPrimary: {
          borderColor: "#BE9063",
          color: "#BE9063",
          "&:hover": {
            borderColor: "#D1A982",
            backgroundColor: "rgba(190, 144, 99, 0.1)",
          },
        },
      },
    },
  },
});

export default theme;
