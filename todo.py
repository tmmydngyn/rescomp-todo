from flask import Flask, render_template, request, jsonify, Response
import os, sys
import sqlite3

from models import Task, db

app = Flask(__name__, static_url_path='/static')

app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'todo.db'),
    DEBUG=True,
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add', methods=['POST'])
def create():
    try:
        description = request.json['description']
        task = Task(description, False, 1)
        db.session.add(task)
        db.session.commit()
    except:
        return Response(response="db error", status=500)

    return Response(response='ok', status=200)

@app.route('/list', methods=['GET'])
def list():
    try:
        items = [{ 'id':          task.id,
                   'description': task.description,
                   'completed':   task.completed } for task in Task.query.all()]
    except:
        return Response(response="db error", status=500)

    return jsonify(items=items)

@app.route('/update', methods=['POST'])
def update():
    try:
        info = request.json
        task = Task.query.filter_by(id=info['id']).first()
        task.completed = info['status']
        db.session.commit()
    except:
        return Response(response="db error", status=500)

    return Response(response="ok", status=200)

@app.route('/delete', methods=['DELETE'])
def delete():
    try:
        task = Task.query.filter_by(id=request.json['id']).first()
        db.session.delete(task)
        db.session.commit()
    except:
        return Response(response='db error', status=500)
    
    return Response(response='ok', status=200)

if __name__ == "__main__":
    # "python app.py restart" to delete db
    restart = False
    if len(sys.argv) > 1:
        if sys.argv[1] == 'restart':
            restart = True

    # Create todo.db if non-existent or if args provided
    if not os.path.exists(app.root_path + '/todo.db') or restart:
        conn = sqlite3.connect('todo.db')
        with open('schema.sql', 'rt') as f:
            schema = f.read()
        conn.executescript(schema)
        print("created todo.db")

    # Run the app
    app.run(debug=True)
