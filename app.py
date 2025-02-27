from flask import Flask,render_template,url_for,flash,session,request,redirect
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db=SQLAlchemy(app)

app.secret_key="1234"

class Todo(db.Model):
    sno=db.Column("sno",db.Integer(),primary_key=True)
    title=db.Column("title",db.String(20))
    description=db.Column("description",db.String(100))

    def __init__(self,title,description):
        self.title=title
        self.description=description

class User(db.Model):
    name=db.Column("name",db.String(20),primary_key=True)
    email=db.Column("email",db.String(20))
    passwd=db.Column("password",db.String(10))

    def __init__(self,name,email,passwd):
        self.name=name
        self.email=email
        self.passwd=passwd

@app.route("/")
def home():
    if "user" in session:
        alltodo=Todo.query.all()
        return render_template("home.html",allTodo=alltodo)
    else:
        return redirect(url_for("login"))

@app.route("/register",methods=["POST","GET"])
def register():
    if(request.method=="GET"):
        return render_template("register.html")
    else:
        
        usr=request.form["name"]
        email=request.form["email"]
        passwd=request.form["password"]

        new_usr=User(usr,email,passwd)

        db.session.add(new_usr)
        db.session.commit()

        session["user"]=usr

        return redirect(url_for("home"))


@app.route("/login",methods=["GET","POST"])
def login():
    if(request.method=="GET"):
        return render_template("login.html")
    else:
        usr=request.form["name"]
        passwd=request.form["password"]
        
        existing_user=User.query.filter_by(name=usr).first()

        if existing_user:
            if(existing_user.passwd==passwd):
                session["user"]=usr
                return redirect(url_for("home"))
            else:
                flash("Wrong Password")
                return redirect(url_for("login"))
        else:
            flash("Register to Access the WebApp")
            return redirect(url_for("register"))
    
@app.route("/logout")
def logout():
    session.pop("user")
    return redirect(url_for("login"))

@app.route("/add", methods=["POST"])
def add():
    if request.method == "POST":
        ttl = request.form["title"]
        desc = request.form["description"]

        new_todo = Todo(title=ttl, description=desc)
        db.session.add(new_todo)
        db.session.commit()

        
    return redirect(url_for("home"))  
    
        


if __name__=="__main__":
   with app.app_context():
        db.create_all()
   app.run(debug=True)