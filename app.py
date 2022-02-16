from crypt import methods
from unicodedata import name
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


my_todo_list = []
@app.route('/', methods=["GET", "POST"])
def home():
    # print(my_todo_list)
    if request.method == "POST":
        newTask = request.form["newTask"]
        if len(newTask) > 0 and newTask not in my_todo_list:
            my_todo_list.append(newTask)

    return render_template("index.html", my_list=my_todo_list, name="Aya")


@app.route("/delete/<task>")
def delete(task):
    my_todo_list.remove(task)
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run()