const express = require('express');
const sql = require('mssql'); // Importa la librería para SQL Server
const path = require('path');
const os = require('os');
const serverName = os.hostname();

const app = express();
const port = 80;

// Configuración de la conexión a SQL Server
// **** ¡IMPORTANTE! Reemplaza estos valores con tus credenciales reales de SQL Server ****
const dbConfig = {
    user: 'Admin', // Por ejemplo, 'sa'
    password: 'testing',
    server: 'localhost', // Por ejemplo, 'localhost' o la IP/nombre de tu servidor SQL
    database: 'db_testing', // El nombre de la base de datos que crearás
    options: {
        encrypt: true, // Para Azure SQL Database (true) o si tu servidor SQL requiere SSL/TLS
        trustServerCertificate: true // Cambiar a false en producción para verificación de certificado
    }
};

// Middleware para parsear JSON en las peticiones
app.use(express.json());
// Middleware para servir archivos estáticos (frontend)
app.use(express.static(path.join(__dirname, 'public')));

// Conectar a la base de datos al iniciar la aplicación
async function connectToDatabase() {
    try {
        await sql.connect(dbConfig);
        console.log('Conexión a SQL Server establecida correctamente.');
    } catch (err) {
        console.error('connectToDatabase:Error al conectar a SQL Server:', err.message);
        // En una app real, aquí manejarías una reconexión o un cierre elegante.
        // Para este ejercicio, simplemente terminamos el proceso si no podemos conectar.
        process.exit(1);
    }
}

// Llama a la función para conectar a la base de datos
connectToDatabase();
// --- Rutas de la API ---

// GET: Obtener todos los activos del portfolio
app.get('/api/portfolio', async (req, res) => {
    try {
        const request = new sql.Request();
        const result = await request.query('SELECT * FROM Assets ORDER BY Name');
        res.json(result.recordset);
    } catch (err) {
        console.error('Error al obtener activos:', err.message);
        res.status(500).json({ message: 'Error interno del servidor al obtener activos.', error: err.message });
    }
});

// POST: Añadir un nuevo activo al portfolio
app.post('/api/portfolio', async (req, res) => {
    const { name, quantity, purchasePrice } = req.body;

    if (!name || typeof quantity === 'undefined' || typeof purchasePrice === 'undefined') {
        return res.status(400).json({ message: 'Todos los campos son obligatorios.' });
    }

    try {
        const request = new sql.Request();
        // Insertar el nuevo activo
        const result = await request
            .input('name', sql.NVarChar, name)
            .input('quantity', sql.Decimal(18, 4), quantity)
            .input('purchasePrice', sql.Decimal(18, 4), purchasePrice)
            .query('INSERT INTO Assets (Name, Quantity, PurchasePrice) VALUES (@name, @quantity, @purchasePrice); SELECT SCOPE_IDENTITY() AS Id;');

        const newAssetId = result.recordset[0].Id;
        res.status(201).json({ id: newAssetId, name, quantity, purchasePrice, message: 'Activo añadido con éxito.' });
    } catch (err) {
        console.error('Error al añadir activo:', err.message);
        res.status(500).json({ message: 'Error interno del servidor al añadir activo.', error: err.message });
    }
});

// DELETE: Eliminar un activo del portfolio por ID
app.delete('/api/portfolio/:id', async (req, res) => {
    const { id } = req.params;

    try {
        const request = new sql.Request();
        const result = await request
            .input('id', sql.Int, id)
            .query('DELETE FROM Assets WHERE Id = @id');

        if (result.rowsAffected[0] === 0) {
            return res.status(404).json({ message: 'Activo no encontrado.' });
        }

        res.status(200).json({ message: 'Activo eliminado con éxito.' });
    } catch (err) {
        console.error('Error al eliminar activo:', err.message);
        res.status(500).json({ message: 'Error interno del servidor al eliminar activo.', error: err.message });
    }
});

// GET: Obtener el nombre o la IP del servidor
app.get('/api/server-info', (req, res) => {
    res.json({
        serverName: serverName,
        message: `¡Hola desde el servidor ${serverName}!`
    });
});

// Iniciar el servidor
app.listen(port, () => {
    console.log(`Servidor de Mi Cartera Personal escuchando en http://localhost:${port}`);
    console.log(`Abre tu navegador en http://localhost:${port}`);
});

// Manejar el cierre de la conexión de la base de datos cuando la aplicación se detiene
process.on('SIGINT', async () => {
    console.log('Cerrando conexión a SQL Server...');
    await sql.close();
    console.log('Conexión a SQL Server cerrada. Saliendo de la aplicación.');
    process.exit(0);
});

