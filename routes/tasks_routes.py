from flask import Blueprint, render_template

# Creamos un Blueprint para las tareas
tasks_bp = Blueprint('tasks', __name__)

@tasks_bp.route('/tareas', methods=['GET'])
def tareas():
    # render_template busca automáticamente dentro de la carpeta 'templates'
    return render_template('tareas.html')