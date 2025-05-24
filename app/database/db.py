from flask import Flask
from flask_mysqldb import MySQL
from dotenv import load_dotenv
import os

load_dotenv()

mysql = MySQL()

def init_database(app: Flask):
    # Mysql Settings
    app.config['MYSQL_USER'] = os.getenv('MYSQL_USER') or 'root'
    app.config['MYSQL_PASSWORD'] = os.getenv('MYSQL_PASSWORD') or ''
    app.config['MYSQL_HOST'] = os.getenv('MYSQL_HOST') or '127.0.0.1'
    app.config['MYSQL_DB'] = os.getenv('MYSQL_DB') or 'db_books'
    app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
    # Iniciar base de datos
    mysql.init_app(app)

    # MySQL Connection
    if app.config['DEBUG'] == True:
        with app.app_context():
            try:
                cur = mysql.connection.cursor()
                sql_path = os.path.join(os.path.dirname(__file__), 'db.sql')
                with open(sql_path, 'r', encoding='utf-8') as sql_file:
                    sql_commands = sql_file.read()
                    for command in sql_commands.split(';'):
                        if command.strip():
                            cur.execute(command)
                mysql.connection.commit()
                print(" * Base de datos generada")
                cur.close()
            except Exception as e:
                print(f"Error: {e}")