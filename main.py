from flask import Flask, request, render_template, url_for
import json
import db.main as DB

app = Flask(__name__)

@app.route("/test")
def helloWorld():
    return json.dumps({"msg":"hello world!"})

@app.route("/")
def requestPage():
    return render_template("request.html")

@app.route("/newRequest",methods=["POST"])
def newRequest():
    requestObj = {
        "name":request.form['name'],
        "vmName":request.form['vmName'],
        "ram":request.form['ram'],
        "diskSize":request.form['diskSize']
    }
    print(requestObj)
    DB.createRequest(requestObj)
    return "okay"

@app.route("/admin")
def adminPage():
    return render_template("admin.html",requests=DB.getRequests())

@app.route("/approve")
def approveRequest():
    _id = request.args.get('_id')
    print(DB.getRequestById(_id))
    return "1"

if __name__ == '__main__':
    app.run(host='localhost',port=2345,debug=True)

