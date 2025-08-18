const express = require('express');
const cors = require('cors');
const { v4: uuidv4 } = require('uuid');

const app = express();
const PORT = process.env.PORT || 3000;

// Middlewares
app.use(cors());
app.use(express.json());

// Base de datos en memoria (simulada)
let accounts = [
  {
    id: "1",
    name: "Juan Pérez",
    email: "juan@example.com",
    balance: 15000.50,
    currency: "USD",
    createdAt: new Date('2024-01-15')
  },
  {
    id: "2",
    name: "María García",
    email: "maria@example.com",
    balance: 8750.25,
    currency: "USD",
    createdAt: new Date('2024-02-01')
  }
];

// Ruta principal
app.get('/', (req, res) => {
  res.json({
    message: 'FinTechPlus API - Servicios Financieros',
    version: '1.0.0',
    endpoints: {
      accounts: '/api/accounts',
      health: '/health'
    }
  });
});

// Health check
app.get('/health', (req, res) => {
  res.json({
    status: 'OK',
    message: 'API funcionando correctamente',
    timestamp: new Date().toISOString(),
    uptime: process.uptime()
  });
});

// RUTAS DE CUENTAS

// GET /api/accounts - Obtener todas las cuentas
app.get('/api/accounts', (req, res) => {
  res.json({
    success: true,
    data: accounts,
    total: accounts.length
  });
});

// POST /api/accounts - Crear nueva cuenta
app.post('/api/accounts', (req, res) => {
  const { name, email, initialBalance = 0, currency = 'USD' } = req.body;
  
  if (!name || !email) {
    return res.status(400).json({
      success: false,
      message: 'Nombre y email son requeridos'
    });
  }
  
  const newAccount = {
    id: uuidv4(),
    name,
    email,
    balance: parseFloat(initialBalance),
    currency,
    createdAt: new Date()
  };
  
  accounts.push(newAccount);
  
  res.status(201).json({
    success: true,
    message: 'Cuenta creada exitosamente',
    data: newAccount
  });
});

// Middleware para rutas no encontradas
app.use('*', (req, res) => {
  res.status(404).json({
    success: false,
    message: 'Endpoint no encontrado',
    availableEndpoints: [
      'GET /',
      'GET /health',
      'GET /api/accounts',
      'POST /api/accounts'
    ]
  });
});

// Middleware de manejo de errores
app.use((error, req, res, next) => {
  console.error('Error:', error);
  res.status(500).json({
    success: false,
    message: 'Error interno del servidor'
  });
});

// Iniciar servidor
app.listen(PORT, '0.0.0.0', () => {
  console.log(`🚀 FinTechPlus API ejecutándose en puerto ${PORT}`);
  console.log(`📊 Health check: http://localhost:${PORT}/health`);
  console.log(`💰 Cuentas: ${accounts.length}`);
});

module.exports = app;