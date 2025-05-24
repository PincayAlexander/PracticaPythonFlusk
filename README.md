# Gestor de Libros

### Instalación
```bash
git clone https://github.com/PincayAlexander/PracticaPythonFlusk.git
cd PracticaPythonFlusk
# En Windows:
bookEnv\Scripts\activate
pip install -r requirements.txt
```

### Base de Datos y usuario administrador
```bash
-- Crear base de datos
CREATE DATABASE db_books;
-- Crear usuario
CREATE USER 'adminUser'@'localhost' IDENTIFIED BY 'pass-123-word';
-- Otorgar todos los privilegios sobre db_books
GRANT ALL PRIVILEGES ON db_books.* TO 'adminUser'@'localhost';
-- Aplicar cambios
FLUSH PRIVILEGES;
```
Por defecto se activa el modo DEBUG y se genera la base de datos desde db.sql

### Ejecutar
```bash
python run.py
```