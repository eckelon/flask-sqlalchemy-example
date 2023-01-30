import os

from flask import redirect, render_template, request

from config import app
from src.model.Todo import create_todo, get_all_todos, get_todo


@app.route("/")
def index():
    todos = get_all_todos()
    return render_template("pages/home.html", todos=todos)


@app.route("/todo/add", methods=["POST"])
def add_todo():
    title = request.form["todo"]
    create_todo(title)
    return redirect(request.referrer)


@app.route("/todo/<int:todo_id>", methods=["GET"])
def get_todo_by_id(todo_id):
    todo = get_todo(id=todo_id)
    return render_template("pages/todo.html", todo=todo)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 3000))
    app.run(debug=True, host="0.0.0.0", port=port)
