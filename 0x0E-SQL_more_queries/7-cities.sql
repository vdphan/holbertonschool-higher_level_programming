-- creates the database hbtn_0d_usa and the table cities
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- use hbtn_od_usa
USE hbtn_0d_usa;
-- create cities table
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
       id INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
       state_id INT NOT NULL,
       name VARCHAR(256) NOT NULL,
       FOREIGN KEY (state_id) REFERENCES states(id)
);
