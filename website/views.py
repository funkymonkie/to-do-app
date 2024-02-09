from flask import Blueprint, render_template, request, redirect, url_for
from .models import Todo
from . import db

my_view = Blueprint("my_view", __name__)


@my_view.route("/")
def home():
    todo_list = Todo.query.all()
    message = request.args.get("message", None)
    print(todo_list)
    return render_template("page1.html", todo_list=todo_list, message=message)


@my_view.route("/add", methods=["POST"])
def add():
    try:
        task = request.form.get("task")
        new_todo = Todo(task=task)
        db.session.add(new_todo)
        db.session.commit()
        return redirect(url_for("my_view.home"))
    except:
        message = "There was an error adding your task."
        return redirect(url_for("my_view.home", message=message))


@my_view.route("/update/<todo_id>", methods=["GET", "POST"])
def update(todo_id):
    if request.method == "POST":
        todo = Todo.query.filter_by(id=todo_id).first()
        todo.complete = not todo.complete
        db.session.commit()
        return redirect(url_for("my_view.home"))


@my_view.route("/edit/<todo_id>")
def edit(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    return render_template("edit.html", todo=todo)


@my_view.route("/edit/<todo_id>", methods=["POST"])
def edit_submit(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    new_task = request.form.get("new_task")
    todo.task = new_task
    db.session.commit()
    return redirect(url_for("my_view.home"))


@my_view.route("/delete/<todo_id>")
def delete(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("my_view.home"))
