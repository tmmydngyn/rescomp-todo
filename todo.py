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

# Handle '/add' request. Fill in this function.
@app.route('/add', methods=['POST'])
def create():
    try:
        description = request.json['description']
        "*** YOUR CODE HERE ***"
    except:
        return Response(response="db error", status=500)

    return Response(response='ok', status=200)

# Handle '/list' request.
# Add a function here.

# Handle '/update' request.
# Add a function here.

# Handle '/delete' request.
# Add a function here.

# Run the application. 
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
