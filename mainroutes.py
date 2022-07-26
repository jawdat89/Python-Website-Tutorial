from flask import Blueprint, render_template
from models import TodoList, TodoItem

routes = Blueprint('routes', __name__)

@routes.route("/")  # Create a page on the first url
def homePage():
  items = [
       "1234",
        "2345",
        "5678"
      ];
  return render_template("homepage.html", todolist = items)