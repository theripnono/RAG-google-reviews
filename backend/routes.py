from flask import Blueprint, request, jsonify
from models import db, Todo, TodoSchema

# Initialize schemas
todo_schema = TodoSchema()
todos_schema = TodoSchema(many=True)

# Create a Blueprint for routes
todo_bp = Blueprint('todo_bp', __name__)

# Route: Create a new todo
@todo_bp.route('/todo', methods=['POST'])
def add_todo():
    title = request.json.get('title')
    description = request.json.get('description')
    new_todo = Todo(title, description)

    db.session.add(new_todo)
    db.session.commit()

    return todo_schema.jsonify(new_todo)

# Route: Get all todos
@todo_bp.route('/todo', methods=['GET'])
def get_todos():
    todos = Todo.query.all()
    return jsonify(todos_schema.dump(todos))

# Route: Get a single todo by ID
@todo_bp.route('/todo/<int:id>', methods=['GET'])
def get_todo(id):
    todo = Todo.query.get_or_404(id)
    return todo_schema.jsonify(todo)

# Route: Update a todo
@todo_bp.route('/todo/<int:id>', methods=['PUT'])
def update_todo(id):
    todo = Todo.query.get_or_404(id)
    todo.title = request.json.get('title')
    todo.description = request.json.get('description')

    db.session.commit()
    return todo_schema.jsonify(todo)

# Route: Delete a todo
@todo_bp.route('/todo/<int:id>', methods=['DELETE'])
def delete_todo(id):
    todo = Todo.query.get_or_404(id)
    db.session.delete(todo)
    db.session.commit()
    return todo_schema.jsonify(todo)
