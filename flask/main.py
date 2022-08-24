from flask import Flask, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)  ##Instanciando objeto da classe flask
db = SQLAlchemy(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///blog.sqlite"

## criando tabela
class Post(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String())
    author = db.Column(db.String())
    content = db.Column(db.String())


try:
    @app.route("/")
    def home():
        name = request.args.get("name")
        #return "<h1>Hello {}</h1>".format(name)
        posts = Post.query.all() ## pegando todos os posts no db
        return render_template("index.html", posts=posts) ## passando templat tag post para front
    
    @app.route("/post/add", methods=["POST"])
    def add_post():
        try:
            form = request.form
            post = Post(title=form["title"], content=form["content"], author=form["author"])
            db.session.add(post)
            db.session.commit()
        except Exception as error:
            print("Error :", error)
        
        return redirect(url_for("home"))
    
    @app.route("/post/<id>/delete")
    def delete_post(id):
        try:
            post = Post.query.get(id)
            db.session.delete(post)
            db.session.commit()
        except Exception as error:
            print("Error :", error)
        
        return redirect(url_for("home"))
    
    @app.route("/post/<id>/edit", methods=["POST", "GET"])
    def edit_post(id):
        if request.method == "POST":
            try:
                post = Post.query.get(id)
                form = request.form
                post.title = form["title"]
                post.content = form["content"]
                post.author = form["author"]
                db.session.commit()
            except Exception as error:
                print("Error edit :", error)
            
            return redirect(url_for("home"))
        else:
            try:
                post = Post.query.get(id)
                return render_template("edit.html", post=post)
            except Exception as error:
                print("Error 3 : ", error)
                
        return redirect(url_for("home"))
    
    db.create_all()
    app.run(debug=True)
except Exception as error:
    print("Error : " , error)