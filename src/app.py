import os

from flask import redirect, render_template, request
from werkzeug.wrappers.response import Response

from config import app
from src.model.Todo import (create_todo, get_all_todos, get_todo,
                            toggle_complete)


@app.route("/")
def index() -> str:
    todos = get_all_todos()
    return render_template("pages/home.html", todos=todos)


@app.route("/todo/add", methods=["POST"])
def add_todo() -> Response:
    title = request.form["todo"]
    create_todo(title)
    return redirect(request.referrer)


@app.route("/todo/<int:todo_id>", methods=["GET"])
def get_todo_by_id(todo_id: int) -> str:
    todo = get_todo(id=todo_id)
    return render_template("pages/todo.html", todo=todo)


@app.route("/todo/<int:todo_id>", methods=["UPDATE"])
def toggle_complete_by_id(todo_id: int) -> dict[str, str]:
    result = toggle_complete(todo_id)
    return result


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 3000))
    app.run(debug=True, host="0.0.0.0", port=port)
