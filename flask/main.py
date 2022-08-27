from flask import Flask, request, render_template, redirect, url_for, jsonify
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
    
    def to_dict(self):
        result = {}
        for key in self.__mapper__.c.keys():
            if getattr(self, key) is not None:
                result[key] = getattr(self, key)
            else:
                result[key] = getattr(self, key)
        return result


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
    
    
    # criando API 
    
    @app.route("/api/posts")
    def api_list_posts():
        try:
            # name = request.args.get("name")
            #return "<h1>Hello {}</h1>".format(name)
            posts = Post.query.all() ## pegando todos os posts no db
            # return render_template("index.html", posts=posts) ## passando templat tag post para front
            # return jsonify({"password" : "teste"})
            return jsonify([post.to_dict() for post in posts])
        except Exception as error:
            print("error" , error)
            return jsonify({[]})
            
    @app.route("/api/post/add", methods=["PUT"])
    def api_add_post():
        try:
            data = request.get_json()
            post = Post(title=data["title"], content=data["content"], author=data["author"])
            db.session.add(post)
            db.session.commit()
            return jsonify({"Success : " : True, "Cadastrado com sucesso" : post.id})
        except Exception as error:
            print("Error :", error)
        
        return jsonify({"Success : " : False})
    
    @app.route("/api/delete/post/<id>", methods=["DELETE"])
    def api_delete_post(id):
        try:
            post = Post.query.get(id)
            db.session.delete(post)
            db.session.commit()
            return jsonify({
                            "Success : " : True,
                            "Id Apagado" : post.id,
                            "Cadastrado por" : post.author
                           })
        except Exception as error:
            print("Error :", error)
        
        return jsonify({"Success : " : False})
    
    @app.route("/api/post/edit/<id>", methods=["PUT"])
    def api_edit_post(id):
        try:
            post = Post.query.get(id)
            data = request.get_json()
            post.title = data["title"]
            post.content = data["content"]
            post.author = data["author"]
            db.session.commit()
            return jsonify({
                            "Success : " : True, 
                            "Editando ID": post.id,
                            "Author" : post.author,
                            "Título do Post" : post.title
                           })
        except Exception as error:
            print("Error edit :", error)
            
            return jsonify({"Success : " : False})
    
    @app.after_request
    def add_header(response):
        response.headers["X-Frame-Options"] = "DENY"
        response.headers["Content-Security-Policy"] = "script-src 'unsafe-inline';"
        response.headers["Access-Control-Allow-Origin"] = "http://example.com" #permite que apenas o example . com possa realizar scripts na pagina
        # response.headers["Access-Control-Allow-Credentials"] = "true" # muito perigoso a ma configuração 
        return response
        
    db.create_all()
    app.run(debug=True)
except Exception as error:
    print("Error : " , error)