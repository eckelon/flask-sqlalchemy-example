from datetime import datetime

from config import db


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(256))
    created = db.Column(db.DateTime, nullable=False)
    completed = db.Column(db.DateTime)


def get_all_todos() -> list[Todo]:
    todos = Todo.query.all()
    return todos


def get_todo(id: int) -> Todo:
    todo = Todo.query.filter_by(id=id).first()
    return todo


def create_todo(title) -> None:
    created = datetime.now()
    todo = Todo(title=title, created=created)
    try:
        db.session.add(todo)
        db.session.commit()
    except Exception as e:
        print(str(e))
        db.session.rollback()
    finally:
        db.session.close()


def toggle_complete(todo_id: int) -> dict:
    todo = get_todo(todo_id)
    completed = datetime.now() if todo.completed is None else None
    todo.completed = completed
    try:
        db.session.commit()
        return {"status": "ok"}
    except Exception as e:
        print(str(e))
        db.session.rollback()
        return {"status": "error"}
    finally:
        db.session.close()
