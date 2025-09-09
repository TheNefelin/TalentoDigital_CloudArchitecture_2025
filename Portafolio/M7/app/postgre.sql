CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    cognito_sub VARCHAR(255) UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS accounts (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id),
    account_number VARCHAR(20) UNIQUE NOT NULL,
    balance DECIMAL(15,2) DEFAULT 0.00
);

CREATE TABLE IF NOT EXISTS transactions (
    id SERIAL PRIMARY KEY,
    from_account_id INTEGER REFERENCES accounts(id),
    to_account_id INTEGER REFERENCES accounts(id),
    amount DECIMAL(15,2) NOT NULL
);

CREATE TABLE IF NOT EXISTS notifications (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    title VARCHAR(255) NOT NULL,
    message TEXT NOT NULL,
    sent_at TIMESTAMP
);

-- Datos de prueba
INSERT INTO users 
  (email, cognito_sub)
VALUES 
  ('test@example.com', 'cognito-sub-123'),
  ('admin@micropay.com', 'cognito-sub-456');

INSERT INTO accounts 
  (user_id, account_number, balance) 
VALUES 
  (1, 'ACC001', 1000.00),
  (2, 'ACC002', 5000.00);

INSERT INTO transactions 
  (from_account_id, to_account_id, amount) 
VALUES 
  (1, 2, 100.00),
  (2, 1, 50.00);

INSERT INTO notifications 
  (user_id, title, message) 
VALUES 
  (1, 'Pago Recibido', 'Recibiste $50.00'),
  (2, 'Pago Enviado', 'Enviaste $100.00');
