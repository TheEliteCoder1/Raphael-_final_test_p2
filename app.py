from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# In-memory storage for tasks (since we're using local storage on frontend,
# this is just for demo - real app uses browser's localStorage)
tasks = []

@app.route('/')
def index():
    """Render the main todo list page"""
    return render_template('index.html')

@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    """API endpoint to get all tasks (for reference)"""
    return jsonify(tasks)

@app.route('/api/tasks', methods=['POST'])
def add_task():
    """API endpoint to add a task (for reference)"""
    data = request.json
    task = {
        'id': len(tasks) + 1,
        'text': data.get('text'),
        'completed': False
    }
    tasks.append(task)
    return jsonify(task), 201

if __name__ == '__main__':
    app.run(debug=True, port=5000)