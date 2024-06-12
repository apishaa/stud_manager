from flask import Flask,render_template,request
from func import *
app=Flask(__name__)
@app.route("/",methods=["POST","GET"])

def home():
    msg=""
    if request.method=="POST":
        msg=request.form["username"]
        # print(request.form["username"])
        # print(request.form["age"])
        # print(request.form["add"])
        # print(request.form["course"])
        # print(request.form["duration"])
        registeration(request.form["username"],request.form["age"],request.form["add"],request.form["course"],request.form["duration"])
    data=read_json()    
    return render_template("index.html",stud=data["students"],msg=msg)

@app.route("/delete/<id>",methods=["POST","GET"])
def delete(id):
    name=delete_stud(id)
    data=read_json()
    return render_template("index.html",stud=data["students"],name=name)
    
    

if __name__=="__main__":
    app.run(debug=True)