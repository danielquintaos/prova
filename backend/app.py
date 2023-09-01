from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os

app = Flask(__name__, template_folder=".")
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:password@postgres:5432/todo'  # or any other URI you are using
db = SQLAlchemy(app)
CORS(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    tasks = db.relationship('Task', backref='user', lazy=True)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(120), nullable=False)
    status = db.Column(db.String(10), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

@app.route('/sign', methods=['GET'])
def sign():
    return render_template('frontend/index.html')

@app.route('/signup', methods=['POST'])
def signup():
    data = request.json
    new_user = User(username=data['username'], password=data['password'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User created"}), 201

@app.route('/tasks', methods=['POST'])
def add_task():
    data = request.json
    new_task = Task(user_id=data['userId'], task=data['task'], status="incomplete")
    db.session.add(new_task)
    db.session.commit()
    return jsonify({"message": "Task added"}), 201

@app.route('/tasks', methods=['GET'])
def get_tasks():
    user_id = request.args.get('userId')
    tasks = Task.query.filter_by(user_id=user_id).all()
    task_list = [{"id": task.id, "task": task.task, "status": task.status} for task in tasks]
    return jsonify(task_list)

@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    task = Task.query.get_or_404(id)
    db.session.delete(task)
    db.session.commit()
    return jsonify({"message": "Task deleted"})


with app.app_context():
    db.create_all()

app.run(debug=True, port=5000, host="0.0.0.0")
