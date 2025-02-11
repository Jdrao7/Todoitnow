from flask import Flask,render_template

app=Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db=SQLAlchemy(app)

class user(db.model):
    title=db.column("title",db.String(20))
    description=db.column("description",db.String(100))

    def __init__(self,title,description)
        self.title=title
        self.description=description

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/login",methods=["GET","POST"])
def login():
    if(request.method=="GET"):
    return render_template("login.html")
    else:
        name=request.form["name"]
        passwd=request.form["password"]


@app.route("/register")
def register():
    return render_template("register.html")

if __name__=="__main__":
    db.create_all()
    app.run()
