from flask import Flask,render_template,request,redirect,url_for
from matplotlib.pyplot import title
import pymysql

app = Flask(__name__)
conn = pymysql.connect(host='localhost',user='root',password='',database='studentdb')

@app.route("/insert",methods=['POST'])
def insert():
    title = "เพิ่มรายชื่อเรียบร้อยแล้ว"
    if request.method == 'POST':
        fname=request.form['fname']
        lname=request.form['lname']
        phone=request.form['phone']
        with conn.cursor() as cursor:
            sql="insert into `studentdb` ( `fname`, `lname`, `phone`) values (%s,%s,%s)"
            cursor.execute(sql,(fname,lname,phone))
            conn.commit()
        return render_template("save.html",title=title)

@app.route('/')
def showDATA():
    with conn:
        cur=conn.cursor()
        cur.execute("select * from studentdb")
        rows=cur.fetchall() 
    return render_template("showdata.html",data=rows)

@app.route('/delete/<string:id>')
def showFrom(id):
    title = "ลบรายชื่อเรียบร้อยแล้ว"
    with conn:
        cur=conn.cursor()
        cur.execute("delete from studentdb where id=%s",id)
        conn.commit()
    return render_template("save.html",title=title)

@app.route('/student')
def show():
    return render_template("addstudent.html")

@app.route('/update1/<string:id>/<string:fname>/<string:lname>/<string:phone>')
def update1(id,fname,lname,phone):
    return render_template("update.html",id=id,fname=fname,lname=lname,phone=phone)

@app.route("/update2",methods=['POST'])
def update2():
    title = "แก้ไขรายชื่อเรียบร้อยแล้ว"
    if request.method == 'POST':
        id_update=request.form['id_up']
        fname=request.form['fname']
        lname=request.form['lname']
        phone=request.form['phone']
        with conn.cursor() as cursor:
            sql="update studentdb set fname=%s,lname=%s,phone=%s where id=%s"
            cursor.execute(sql, (fname,lname,phone,id_update) )
            conn.commit()
        return render_template("save.html",title=title)

        
if __name__ == '__main__':
    app.run(debug=True)
