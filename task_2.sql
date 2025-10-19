-- SELECT DATABASE TO USE
USE alx_book_store;

-- 1. Authors Table
CREATE TABLE IF NOT EXISTS Authors (
    author_id INT NOT NULL AUTO_INCREMENT,
    author_name VARCHAR(215) NOT NULL,
    PRIMARY KEY (author_id)
);

-- 2. Books Table
CREATE TABLE IF NOT EXISTS Books (
    book_id INT NOT NULL AUTO_INCREMENT,
    title VARCHAR(130) NOT NULL,
    author_id INT NOT NULL,
    price DOUBLE NOT NULL,
    publication_date DATE,
    PRIMARY KEY (book_id),
    FOREIGN KEY (author_id) REFERENCES Authors(author_id)
);

-- 3. Customers Table
CREATE TABLE IF NOT EXISTS Customers (
    customer_id INT NOT NULL AUTO_INCREMENT,
    customer_name VARCHAR(215) NOT NULL,
    email VARCHAR(215) NOT NULL UNIQUE,
    address TEXT,
    PRIMARY KEY (customer_id)
);

-- 4. Orders Table
CREATE TABLE IF NOT EXISTS Orders (
    order_id INT NOT NULL AUTO_INCREMENT,
    customer_id INT NOT NULL,
    order_date DATE NOT NULL,
    PRIMARY KEY (order_id),
    FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
);

-- 5. Order_Details Table
CREATE TABLE IF NOT EXISTS Order_Details (
    orderdetailid INT NOT NULL AUTO_INCREMENT,
    order_id INT NOT NULL,
    book_id INT NOT NULL,
    quantity DOUBLE NOT NULL,
    PRIMARY KEY (orderdetailid),
    FOREIGN KEY (order_id) REFERENCES Orders(order_id),
    FOREIGN KEY (book_id) REFERENCES Books(book_id)
);
