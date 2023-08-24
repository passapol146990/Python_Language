from flask import Flask,render_template,session,request,url_for
from flask_wtf import FlaskForm
from wtforms import SubmitField,StringField,IntegerField
import pymysql

app = Flask(__name__)
app.config['SECRET_KEY'] = 'phol'

conn = pymysql.connect(host='localhost',user='root',password='',database='studentdb')

class myform(FlaskForm):
    name = StringField('ชื่อ')
    address = StringField('ที่อยู่')
    salary = IntegerField('เงินเดือน')
    submit = SubmitField('บันทึก')

@app.route('/',methods=['GET', 'POST'])
def index():
    cur = conn.cursor()
    cur.execute('SELECT * FROM databd1')
    rows = cur.fetchall() 
    return render_template('home.html',data=rows)

@app.route('/form',methods=['GET', 'POST'])
def showform():
    form = myform()
    if form.validate_on_submit():
        session['name'] = form.name.data
        session['address'] = form.address.data
        session['salary'] = form.salary.data
        form.name.data = ''
        form.address.data = ''
        form.salary.data = ''

        cur = conn.cursor()
        cur.execute('INSERT INTO databd1(name,address,salary) VALUES(%s,%s,%s)',(session['name'],session['address'],session['salary']))
        conn.commit()

        cur1 = conn.cursor()
        cur1.execute('SELECT * FROM databd1')
        rows = cur1.fetchall()
        return render_template('home.html',data=rows)

    return render_template('showform.html',form=form)

@app.route('/delete/<string:id_data>',methods=['GET'])
def delete(id_data):
    cur = conn.cursor()
    cur.execute('DELETE FROM databd1 WHERE id=%s',id_data)
    conn.commit()

    cur1 = conn.cursor()
    cur1.execute('SELECT * FROM databd1')
    rows = cur1.fetchall()

    return render_template('home.html',data=rows)

@app.route('/update',methods=['post'])
def update():
    if request.method == 'POST':
        id_up = request.form['id']
        name_up = request.form['name']
        address_up = request.form['address']
        salary_up = request.form['salary']

        cur = conn.cursor()
        cur.execute('UPDATE databd1 SET name=%s, address=%s,salary=%s WHERE id=%s',(name_up,address_up,salary_up,id_up))
        conn.commit()

        cur1 = conn.cursor()
        cur1.execute('SELECT * FROM databd1')
        rows = cur1.fetchall()
        return render_template('home.html',data=rows)

if __name__ == '__main__':
    app.run(debug=True)

