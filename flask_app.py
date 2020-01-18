
from flask import Flask, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
import git

app = Flask(__name__)
app.config["DEBUG"] = True

SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
    username="MyFridge",
    password="DBfood2020",
    hostname="MyFridge.mysql.pythonanywhere-services.com",
    databasename="MyFridge$Groceries",
)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Groceries(db.Model):

    __tablename__ = "Groceries"

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(4096))
    quantity = db.Column(db.Integer)

@app.route('/update_server', methods=['POST'])
def webhook():
    if request.method == 'POST':
        repo = git.Repo('path/to/git_repo')
        origin = repo.remotes.origin

    origin.pull()
    return 'Updated PythonAnywhere successfully', 200
#    else:
#        return 'Wrong event type', 400


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("main_page.html", groceries=Groceries.query.all())

    groceries_name = Groceries(content=request.form["contents"])
    groceries_quantity = Groceries(quantity=request.form["contents"])
    db.session.add(groceries)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    db.create_all()
    app.run()


