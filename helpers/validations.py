def validar_credenciales(datos):
    """
    Verifica que los datos contengan usuario y contraseña.
    Retorna un mensaje de error y un código HTTP si falta algo, o None si está OK.
    """
    if not datos:
        return {"error": "No se enviaron datos en formato JSON"}, 400
        
    usuario = datos.get('usuario')
    contrasena = datos.get('contraseña')
    
    if not usuario or not contrasena:
        return {"error": "Se requiere usuario y contraseña"}, 400
        
    return None