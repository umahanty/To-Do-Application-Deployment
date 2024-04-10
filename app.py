# app.py (Flask backend)

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

tasks = []

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add_task', methods=['POST'])
def add_task():
    task_content = request.form['content']
    tasks.append({'content': task_content, 'completed': False})
    return jsonify({'message': 'Task added successfully'})

@app.route('/mark_complete/<int:task_index>', methods=['PUT'])
def mark_complete(task_index):
    if task_index < len(tasks):
        tasks[task_index]['completed'] = True
        return jsonify({'message': 'Task marked as completed'})
    else:
        return jsonify({'error': 'Task index out of range'}), 404

@app.route('/delete_task/<int:task_index>', methods=['DELETE'])
def delete_task(task_index):
    if task_index < len(tasks):
        del tasks[task_index]
        return jsonify({'message': 'Task deleted successfully'})
    else:
        return jsonify({'error': 'Task index out of range'}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

