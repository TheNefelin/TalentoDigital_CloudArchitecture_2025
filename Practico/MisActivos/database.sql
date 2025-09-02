-- Script para crear la base de datos y la tabla de activos
-- Ejecuta este script en tu servidor SQL Server (por ejemplo, usando SQL Server Management Studio o Azure Data Studio)

-- 1. Crear la base de datos si no existe
IF NOT EXISTS (SELECT name FROM sys.databases WHERE name = 'PortfolioDB')
BEGIN
    CREATE DATABASE PortfolioDB;
END;
GO

-- 2. Usar la base de datos recién creada o existente
USE PortfolioDB;
GO

-- 3. Crear la tabla Assets si no existe
IF NOT EXISTS (SELECT * FROM sysobjects WHERE id = OBJECT_ID(N'[dbo].[Assets]') AND OBJECTPROPERTY(id, N'IsUserTable') = 1)
BEGIN
    CREATE TABLE Assets (
        Id INT IDENTITY(1,1) PRIMARY KEY, -- ID auto-incrementable
        Name NVARCHAR(50) NOT NULL,       -- Nombre del activo (ej: "AAPL", "BTC")
        Quantity DECIMAL(18, 4) NOT NULL, -- Cantidad de unidades del activo
        PurchasePrice DECIMAL(18, 4) NOT NULL, -- Precio de compra por unidad
        CreatedAt DATETIME DEFAULT GETDATE() -- Fecha de creación del registro
    );
END;
GO

-- Puedes insertar algunos datos de ejemplo si lo deseas para probar
-- INSERT INTO Assets (Name, Quantity, PurchasePrice) VALUES ('AAPL', 10.5, 150.25);
-- INSERT INTO Assets (Name, Quantity, PurchasePrice) VALUES ('MSFT', 5.0, 300.75);
