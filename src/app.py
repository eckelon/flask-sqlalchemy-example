import os
from config import app
from flask import render_template, request
from src.model.Todo import create_todo, get_todo


@app.route("/")
def index():
    return render_template("pages/home.html")


@app.route("/todo/add", methods=["GET", "POST"])
def add_todo():
    if request.method == "GET":
        return render_template("pages/add-todo.html")

    title = request.form["todo"]
    create_todo(title)

    return render_template("pages/add-todo.html")


@app.route("/todo/<int:todo_id>", methods=["GET"])
def get_todo_by_id(todo_id):
    todo = get_todo(id=todo_id)
    return render_template("pages/todo.html", todo=todo)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 3000))
    app.run(debug=True, host="0.0.0.0", port=port)
