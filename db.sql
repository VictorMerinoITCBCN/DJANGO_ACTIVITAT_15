CREATE TABLE User (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    lastName VARCHAR(255) NOT NULL
);

CREATE TABLE Product (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    description TEXT NOT NULL,
    price DECIMAL(10,2) NOT NULL CHECK (price >= 0), 
    stock INT NOT NULL CHECK (stock >= 0),
    category VARCHAR(255) NOT NULL,
    img VARCHAR(500)
);

CREATE TABLE Cart (
    id INT AUTO_INCREMENT PRIMARY KEY,
    userId INT NOT NULL,
    createdAt DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (userId) REFERENCES User(id) ON DELETE CASCADE
);

CREATE TABLE CartItem (
    id INT AUTO_INCREMENT PRIMARY KEY,
    cartId INT NOT NULL,
    productId INT NOT NULL,
    quantity INT NOT NULL CHECK (quantity > 0),
    FOREIGN KEY (cartId) REFERENCES Cart(id) ON DELETE CASCADE,
    FOREIGN KEY (productId) REFERENCES Product(id) ON DELETE CASCADE
);

CREATE TABLE `Order` (
    id INT AUTO_INCREMENT PRIMARY KEY,
    userId INT NOT NULL,
    totalPrice DECIMAL(10,2) NOT NULL CHECK (totalPrice >= 0),
    status ENUM('pending', 'paid', 'shipped', 'delivered', 'cancelled') NOT NULL DEFAULT 'pending',
    createdAt DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (userId) REFERENCES User(id) ON DELETE CASCADE
);

CREATE TABLE OrderItem (
    id INT AUTO_INCREMENT PRIMARY KEY,
    orderId INT NOT NULL,
    productId INT NOT NULL,
    quantity INT NOT NULL CHECK (quantity > 0),
    FOREIGN KEY (orderId) REFERENCES `Order`(id) ON DELETE CASCADE,
    FOREIGN KEY (productId) REFERENCES Product(id) ON DELETE CASCADE
);

CREATE TABLE Payment (
    id INT AUTO_INCREMENT PRIMARY KEY,
    orderId INT NOT NULL,
    cardNumber VARCHAR(16) NOT NULL, 
    expirationDate DATE NOT NULL,
    cvc VARCHAR(4) NOT NULL, 
    status ENUM('pending', 'approved', 'rejected') NOT NULL DEFAULT 'pending',
    FOREIGN KEY (orderId) REFERENCES `Order`(id) ON DELETE CASCADE
);
