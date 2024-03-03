from quickchart import QuickChart

from flask import Flask , render_template, request

app = Flask(__name__)

@app.route("/" ,methods = ['POST', 'GET'])
def home():
    return render_template("home.html") 

@app.route("/fifo",methods = ['POST', 'GET'])
def fifo():
    return render_template("fifo.html") 

@app.route("/sjf",methods = ['POST', 'GET'])
def sjf():
    return render_template("sjf.html") 

@app.route("/priority",methods = ['POST', 'GET'])
def priority():
    return render_template("priority.html") 


@app.route("/roundRobin",methods = ['POST', 'GET'])
def roundRobin():
    return render_template("roundRobin.html") 


if __name__ == "__main__":
    app.run(debug=True)