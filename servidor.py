from flask import Flask
import sqlite3

# Importamos el Blueprint que acabamos de crear
from routes.auth_routes import auth_bp
from routes.tasks_routes import tasks_bp

app = Flask(__name__)

# Registramos el blueprint en la app principal
app.register_blueprint(auth_bp)
app.register_blueprint(tasks_bp)

def init_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            usuario TEXT UNIQUE NOT NULL,
            contrasena TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

if __name__ == '__main__':
    init_db()
    app.run(debug=True, port=5000)