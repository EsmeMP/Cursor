from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from datetime import datetime
import json
import os

app = Flask(__name__)
app.secret_key = 'task_manager_secret_key_2024'  # Cambia esto en producción

# Configuración
app.config['DEBUG'] = True
app.config['TASKS_FILE'] = 'tasks.json'

# Lista de tareas en memoria (en producción usarías una base de datos)
tasks = []

def load_tasks():
    """Cargar tareas desde archivo JSON"""
    global tasks
    if os.path.exists(app.config['TASKS_FILE']):
        try:
            with open(app.config['TASKS_FILE'], 'r', encoding='utf-8') as f:
                tasks = json.load(f)
        except:
            tasks = []
    else:
        tasks = []

def save_tasks():
    """Guardar tareas en archivo JSON"""
    with open(app.config['TASKS_FILE'], 'w', encoding='utf-8') as f:
        json.dump(tasks, f, ensure_ascii=False, indent=2)

# Cargar tareas al iniciar
load_tasks()

# Rutas principales
@app.route('/')
def index():
    """Página principal - Lista de tareas"""
    return render_template('index.html', tasks=tasks, title='Gestor de Tareas')

@app.route('/add_task', methods=['POST'])
def add_task():
    """Agregar nueva tarea"""
    title = request.form.get('title', '').strip()
    description = request.form.get('description', '').strip()
    priority = request.form.get('priority', 'media')
    
    if not title:
        flash('El título de la tarea es obligatorio', 'error')
        return redirect(url_for('index'))
    
    new_task = {
        'id': len(tasks) + 1,
        'title': title,
        'description': description,
        'priority': priority,
        'status': 'pendiente',
        'created_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'completed_at': None
    }
    
    tasks.append(new_task)
    save_tasks()
    flash('Tarea agregada exitosamente', 'success')
    return redirect(url_for('index'))

@app.route('/complete_task/<int:task_id>')
def complete_task(task_id):
    """Marcar tarea como completada"""
    for task in tasks:
        if task['id'] == task_id:
            task['status'] = 'completada'
            task['completed_at'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            save_tasks()
            flash('Tarea marcada como completada', 'success')
            break
    return redirect(url_for('index'))

@app.route('/delete_task/<int:task_id>')
def delete_task(task_id):
    """Eliminar tarea"""
    global tasks
    tasks = [task for task in tasks if task['id'] != task_id]
    save_tasks()
    flash('Tarea eliminada exitosamente', 'success')
    return redirect(url_for('index'))

@app.route('/edit_task/<int:task_id>', methods=['GET', 'POST'])
def edit_task(task_id):
    """Editar tarea existente"""
    task = None
    for t in tasks:
        if t['id'] == task_id:
            task = t
            break
    
    if not task:
        flash('Tarea no encontrada', 'error')
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        task['title'] = request.form.get('title', '').strip()
        task['description'] = request.form.get('description', '').strip()
        task['priority'] = request.form.get('priority', 'media')
        
        if not task['title']:
            flash('El título de la tarea es obligatorio', 'error')
            return render_template('edit_task.html', task=task, title='Editar Tarea')
        
        save_tasks()
        flash('Tarea actualizada exitosamente', 'success')
        return redirect(url_for('index'))
    
    return render_template('edit_task.html', task=task, title='Editar Tarea')

@app.route('/api/tasks')
def api_tasks():
    """API endpoint para obtener todas las tareas"""
    return jsonify(tasks)

@app.route('/api/task/<int:task_id>')
def api_task(task_id):
    """API endpoint para obtener una tarea específica"""
    task = next((t for t in tasks if t['id'] == task_id), None)
    if task:
        return jsonify(task)
    return jsonify({'error': 'Tarea no encontrada'}), 404

# Manejo de errores
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', title='Página no encontrada'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html', title='Error interno'), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
