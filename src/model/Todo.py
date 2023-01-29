from config import db


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(256))


def get_todo(id):
    todo = Todo.query.filter_by(id=id).first()
    return todo


def create_todo(title):
    todo = Todo(title=title)
    try:
        db.session.add(todo)
        db.session.commit()
    except Exception as e:
        print(e)
        db.session.rollback()
    finally:
        db.session.close()
