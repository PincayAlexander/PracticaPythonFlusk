USE db_books;

CREATE TABLE IF NOT EXISTS books (
  id INTEGER PRIMARY KEY AUTO_INCREMENT,
  title VARCHAR(255) NOT NULL,
  author VARCHAR(255) NOT NULL,
  genre VARCHAR(100),
  publication DATE,
  rating DECIMAL(2,1),
  status ENUM('leido', 'por_leer'),
  notes TEXT
);
