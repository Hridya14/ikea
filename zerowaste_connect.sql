-- Create Database
CREATE DATABASE zerowaste_connect;

USE zerowaste_connect;

-- =========================
-- 1. Donors Table
-- =========================

CREATE TABLE donors (
    donor_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- =========================
-- 2. Food Listings Table
-- =========================

CREATE TABLE food_listings (
    food_id INT AUTO_INCREMENT PRIMARY KEY,
    donor_id INT,
    food_name VARCHAR(100) NOT NULL,
    quantity INT NOT NULL,
    ingredients TEXT,
    location VARCHAR(150),
    expiry_time DATETIME NOT NULL,
    status ENUM('Available','Claimed') DEFAULT 'Available',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (donor_id) REFERENCES donors(donor_id)
        ON DELETE CASCADE
);

-- =========================
-- 3. Ratings Table
-- =========================

CREATE TABLE ratings (
    rating_id INT AUTO_INCREMENT PRIMARY KEY,
    food_id INT,
    rating INT CHECK (rating >= 1 AND rating <= 5),
    rated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (food_id) REFERENCES food_listings(food_id)
        ON DELETE CASCADE
);
