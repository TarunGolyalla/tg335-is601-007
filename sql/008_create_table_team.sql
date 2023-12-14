CREATE TABLE 
	IS601_Team(
    id INT PRIMARY KEY,
    created TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    modified TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    name VARCHAR(255),
    code VARCHAR(10),
    country VARCHAR(50),
    founded INT,
    national BOOLEAN,
    logo_url VARCHAR(255),
    venue_id INT,
    FOREIGN KEY (venue_id) REFERENCES IS601_Venue(id)
);