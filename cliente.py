import requests

BASE_URL = "http://localhost:5000"

def mostrar_menu():
    print("\n==============================")
    print("   SISTEMA DE GESTIÓN DE TAREAS")
    print("==============================")
    print("1. Registrar nuevo usuario")
    print("2. Iniciar sesión")
    print("3. Salir")

def mostrar_respuesta(respuesta):
    """Función auxiliar para mostrar las respuestas del servidor de forma ordenada"""
    print(f"\n--- Código de Estado: {respuesta.status_code} ---")
    try:
        datos = respuesta.json()
        if "mensaje" in datos:
            print(f" Éxito: {datos['mensaje']}")
        elif "error" in datos:
            print(f" Error: {datos['error']}")
        else:
            print(datos)
    except ValueError:
        print(respuesta.text)

def registrarse():
    print("\n--- REGISTRO DE USUARIO ---")
    usuario = input("Ingrese su usuario: ")
    contrasena = input("Ingrese su contraseña: ")
    
    try:
        respuesta = requests.post(f"{BASE_URL}/registro", json={
            "usuario": usuario,
            "contraseña": contrasena
        })
        mostrar_respuesta(respuesta)
    except requests.exceptions.ConnectionError:
        print("\n[Error] No se pudo conectar con el servidor. ¿Está encendido?")

def iniciar_sesion():
    print("\n--- INICIO DE SESIÓN ---")
    usuario = input("Ingrese su usuario: ")
    contrasena = input("Ingrese su contraseña: ")
    
    try:
        respuesta = requests.post(f"{BASE_URL}/login", json={
            "usuario": usuario,
            "contraseña": contrasena
        })
        mostrar_respuesta(respuesta)
        
        # Si el login es exitoso (200), permitimos ver las tareas
        if respuesta.status_code == 200:
            ver_tareas = input("\n¿Desea acceder a la sección de tareas? (s/n): ")
            if ver_tareas.lower() == 's':
                res_tareas = requests.get(f"{BASE_URL}/tareas")
                print(f"\n--- [GET /tareas] Estado: {res_tareas.status_code} ---")
                
                print("Contenido HTML recibido del servidor:")
                print(res_tareas.text)
                
    except requests.exceptions.ConnectionError:
        print("\n[Error] No se pudo conectar con el servidor. ¿Está encendido?")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-3): ")
        
        if opcion == "1":
            registrarse()
        elif opcion == "2":
            iniciar_sesion()
        elif opcion == "3":
            print("\n¡Gracias por usar el sistema! Saliendo...")
            break
        else:
            print("\nOpción inválida. Por favor, elija entre 1 y 3.")

if __name__ == "__main__":
    main()