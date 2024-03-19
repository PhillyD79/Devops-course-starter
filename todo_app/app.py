from flask import Flask, render_template, request , redirect
from todo_app.flask_config import Config
from todo_app.data.session_items import get_items
from todo_app.data.trello_item import add_items

import os
app = Flask(__name__)
app.config.from_object(Config())

print(os.getenv("TRELLO_API_KEY"))

@app.route('/')
def index():
    items = get_items()
    return render_template("index.html", template_items = items)

@app.route('/add-todo' , methods=["POST"])
def add_todo():
    new_todo_title = request.form.get ("title")
    add_items(new_todo_title)
    return redirect('/')