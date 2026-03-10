CREATE SCHEMA IF NOT EXISTS book_store;

USE book_store;

CREATE TABLE IF NOT EXISTS members (
    fname VARCHAR(50) NOT NULL,
    lname VARCHAR(50) NOT NULL,
    address VARCHAR(50) NOT NULL,
    city VARCHAR(30) NOT NULL,
    zip INT NOT NULL,
    phone VARCHAR(15),
    email VARCHAR(40) UNIQUE NOT NULL,
    userid INT AUTO_INCREMENT PRIMARY KEY,
    password VARCHAR(200) NOT NULL
);

CREATE TABLE IF NOT EXISTS books (
    isbn CHAR(10) PRIMARY KEY,
    author VARCHAR(100) NOT NULL,
    title VARCHAR(200) NOT NULL,
    price FLOAT NOT NULL,
    subject VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS cart (
    userid INT NOT NULL,
    isbn CHAR(10) NOT NULL,
    qty INT NOT NULL,

    PRIMARY KEY (userid, isbn),
    FOREIGN KEY (userid) REFERENCES members(userid),
    FOREIGN KEY (isbn) REFERENCES books(isbn)
);

CREATE TABLE IF NOT EXISTS orders (
    ono INT AUTO_INCREMENT PRIMARY KEY,
    userid INT NOT NULL,
    created DATE,
    shipAddress VARCHAR(50),
    shipCity VARCHAR(30),
    shipZip INT,

    FOREIGN KEY (userid) REFERENCES members(userid)
);

CREATE TABLE IF NOT EXISTS odetails (
    ono INT NOT NULL,
    isbn CHAR(10) NOT NULL,
    qty INT NOT NULL,
    amount FLOAT NOT NULL,

    PRIMARY KEY (ono, isbn),
    FOREIGN KEY (ono) REFERENCES orders(ono),
    FOREIGN KEY (isbn) REFERENCES books(isbn)
);