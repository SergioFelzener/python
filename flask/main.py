from flask import Flask

app = Flask(__name__)

try:
    
    @app.route("/")
    def home():
        return "TESTE"

    app.run(debug=True)

except Exception as error:
    print("Error : " , error)