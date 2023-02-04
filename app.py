from flask import Flask,render_template,request

import requests

app=Flask(__name__)

@app.route("/")
def Sample():
    x=dict([('id', '1'), ('name', 'Sakthivel M'), ('mobile', '9843659321')])
    print(x)
    return x.get("id")

@app.route("/<num1>,<num2>")
def Add(num1,num2):
    return str(int(num1)+int(num2))

l=[]
@app.route("/form",methods=["POST","GET"])
def Form():
    if request.method=="POST":
        id=request.form.get("id")
        name=request.form.get("name")
        mobile=request.form.get("mobile")
        dic={"id":id,"name":name,"mobile":mobile}
        l.append(dic)
        return render_template("table.html",data=l)
    return render_template("index.html")

@app.route("/api",methods=["POST","GET"])
def Api():
    id=request.json
    return str(type(id))

@app.route("/api/<name1>,<name2>",methods=["POST"])
def ApiNum(name1,name2):
    concat=name1+name2
    return concat

@app.route("/apidata",methods=["POST","GET"])
def ApiData():
    # data=request.json
    # l.append(data)
    id=request.json.get("id")
    name=request.json.get("name")
    mobile=request.json.get("mobile")
    dic={"id":id,"name":name,"mobile":mobile}
    l.append(dic)
    return render_template("table.html",data=l)

@app.route("/naveReport/<code>")
def NavReport(code):
    url="https://api.mfapi.in/mf/"+str(code)
    resp=requests.get(url)
    data=resp.json()

    return data


if __name__=="__main__":
    app.run(debug=True)