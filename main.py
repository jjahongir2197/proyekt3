from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
db = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(200))
    completed = db.Column(db.Boolean, default=False)

def complete_task(task_id):
    task = Task.query.get(task_id)

    if task:
        task.completed = True
        db.session.commit()

with app.app_context():
    db.create_all()

    t1 = Task(title="Learn SQLAlchemy")
    t2 = Task(title="Build Flask API")

    db.session.add_all([t1, t2])
    db.session.commit()

    complete_task(1)

    tasks = Task.query.all()

    for t in tasks:
        print(t.title, t.completed)
