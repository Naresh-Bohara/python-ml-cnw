/*
CREATE DATABASE database_name;
*/
CREATE DATABASE store;


/*
USE database_name;
*/
USE store;


/*
CREATE TABLE table_name(
 column datatype,
 column datatype
);
*/
CREATE TABLE product (
 id INT,
 name VARCHAR(50),
 price DECIMAL(10,2),
 category VARCHAR(50)
);


/*
INSERT INTO table_name(columns)
VALUES(values);
*/
INSERT INTO product (id, name, price, category)
VALUES (1, 'Drone', 15000.00, 'Electronics');


/*
SELECT * FROM table_name;
*/
SELECT * FROM product;


/*
ALTER TABLE table_name
ADD column_name datatype;
*/
ALTER TABLE product
ADD brand VARCHAR(50);


/*
ALTER TABLE table_name
DROP COLUMN column_name;
*/
ALTER TABLE product
DROP COLUMN category;


/*
ALTER TABLE table_name
RENAME COLUMN old_name TO new_name;
*/
ALTER TABLE product
RENAME COLUMN name TO product_name;


/*
ALTER TABLE table_name
CHANGE old_name new_name datatype;
*/
ALTER TABLE product
CHANGE product_name name VARCHAR(60);


/*
UPDATE table_name
SET column=value
WHERE condition;
*/
UPDATE product
SET brand = 'DJI'
WHERE id = 1;


/*
DROP TABLE table_name;
*/
DROP TABLE product;


/*
DROP DATABASE database_name;
*/
DROP DATABASE store;