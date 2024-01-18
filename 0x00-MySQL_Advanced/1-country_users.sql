-- Create table with params
CREATE TABLE IF NOT EXISTS users (
        id INT UNIQUE AUTO_INCREMENT PRIMARY KEY,
        email VARCHAR(255) NOT NULL UNIQUE,
        name VARCHAR(255),
	country VARCHAR(2) DEFAULT 'US' NOT NULL CHECK (
		country IN ('US', 'CO', 'TN'))
)
