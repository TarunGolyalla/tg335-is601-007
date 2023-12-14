CREATE TABLE 
	IS601_Venue (
    id INT PRIMARY KEY,
    created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    modified TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    name VARCHAR(255),
    address VARCHAR(255),
    city VARCHAR(100),
    capacity INT,
    surface VARCHAR(50),
    image_url VARCHAR(255)
);