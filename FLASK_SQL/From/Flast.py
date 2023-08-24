from flask import Flask, flash,render_template,request,flash
import templates
#from flask_wtf import flaskForm
app = Flask(__name__)
@app.route('/')
def index():
    return render_template("index.html")
@app.route('/about')

def about():
    return  render_template("about.html")
@app.route('/shop')

def shop():
    return render_template("shop.html")
@app.route('/item')
def item():
    return render_template("item.html")

@app.route('/admin',methods=['GET','POST'])
def admin():
    return render_template("admin.html")

@app.route('/sendData')
def admindata():
    fname=request.args.get('fname')
    age=request.args.get('age')
    description=request.args.get('description')
    return render_template("admindata.html",data={"age":age,"name":fname,"description":description})
if __name__ == "__main__":
    app.run(debug=True)