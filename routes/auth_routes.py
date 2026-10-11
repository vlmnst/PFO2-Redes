from flask import Blueprint, request, jsonify
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash
from helpers.validations import validar_credenciales

# Creamos un Blueprint llamado 'auth'
auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/registro', methods=['POST'])
def registro():
    datos = request.get_json()
    error_validacion = validar_credenciales(datos)
    if error_validacion:
        return jsonify(error_validacion[0]), error_validacion[1]
    
    usuario = datos.get('usuario')
    contrasena = datos.get('contraseña')
    contrasena_hasheada = generate_password_hash(contrasena, method='pbkdf2:sha256')
    
    try:
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO usuarios (usuario, contrasena) VALUES (?, ?)', (usuario, contrasena_hasheada))
        conn.commit()
        conn.close()
    except sqlite3.IntegrityError:
        return jsonify({"error": "El nombre de usuario ya está en uso"}), 400

    return jsonify({"mensaje": "Usuario registrado exitosamente"}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    datos = request.get_json()
    error_validacion = validar_credenciales(datos)
    if error_validacion:
        return jsonify(error_validacion[0]), error_validacion[1]
        
    usuario = datos.get('usuario')
    contrasena = datos.get('contraseña')
        
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT contrasena FROM usuarios WHERE usuario = ?', (usuario,))
    resultado = cursor.fetchone()
    conn.close()
    
    if resultado is None:
        return jsonify({"error": "Usuario o contraseña incorrectos"}), 401
        
    contrasena_hasheada = resultado[0]
    
    if check_password_hash(contrasena_hasheada, contrasena):
        return jsonify({"mensaje": "¡Inicio de sesión exitoso! Bienvenido al sistema."}), 200
    else:
        return jsonify({"error": "Usuario o contraseña incorrectos"}), 401