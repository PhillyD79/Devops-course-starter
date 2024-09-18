from flask import Flask, render_template, request , redirect
from todo_app.flask_config import Config

from todo_app.data.trello_item import add_items, get_items, complete_item

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config())

print(os.getenv("TRELLO_API_KEY"))

@app.route('/')
def index():
    items = get_items()
    view_model = ViewModel(items)
    return render_template("index.html", view_model = view_model)

@app.route('/add-todo' , methods=["POST"])
def add_todo():
    new_todo_title = request.form.get ("title")
    add_items(new_todo_title)
    return redirect('/')

@app.route('/complete-item/<todo_id>' , methods=["POST"])
def complete_todo(todo_id):
    complete_item(todo_id)
    return redirect('/')

return app