CREATE DATABASE IF NOT EXISTS autoparts;

USE autoparts;

CREATE TABLE IF NOT EXISTS users(
    user_id int NOT NULL UNIQUE AUTO_INCREMENT,
    user_name VARCHAR(255) NOT NULL,
    user_email VARCHAR(255) NOT NULL,
    user_password VARCHAR(255) NOT NULL,
    PRIMARY KEY (user_id)
);

CREATE TABLE IF NOT EXISTS brands(
    brand_id INT NOT NULL UNIQUE AUTO_INCREMENT,
    brand_name VARCHAR(255) UNIQUE NOT NULL,
    brand_code VARCHAR(3) UNIQUE NOT NULL,
    PRIMARY KEY (brand_id)
);

CREATE TABLE IF NOT EXISTS models(
    model_id INT UNIQUE NOT NULL AUTO_INCREMENT,
    model_name VARCHAR(255) UNIQUE NOT NULL,
    model_code VARCHAR(3) UNIQUE NOT NULL,
    brand_code VARCHAR(3),
    PRIMARY KEY (model_id),
    FOREIGN KEY (brand_code) REFERENCES brands(brand_code)
);

CREATE TABLE IF NOT EXISTS parts(
    part_id INT UNIQUE NOT NULL AUTO_INCREMENT,
    part_name VARCHAR(255) UNIQUE NOT NULL,
    part_code VARCHAR(3) UNIQUE NOT NULL,
    part_price DECIMAL NOT NULL,
    part_amount INT NOT NULL,
    model_code VARCHAR(3),
    PRIMARY KEY (part_id),
    FOREIGN KEY (model_code) REFERENCES models(model_code)
);