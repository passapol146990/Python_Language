from flask import Flask,render_template,session,flash
from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,\
RadioField,SubmitField,SelectField,BooleanField
from flask_bootstrap import Bootstrap


app = Flask(__name__)
Bootstrap(app)

app.config['SECRET_KEY'] = 'mykey'

class myform(FlaskForm):
    text = StringField('ป้อนชื่อ')
    button = SubmitField('save')
    textarea = TextAreaField('address')
    select = SelectField('Language',choices=[('python', 'python'), ('Flask','Flask'),('html', 'html'), ('sql','SQL')])
    radio = RadioField('เพศ',choices=[('man','ชาย'),('girl','หญิง'),('other','อื่นๆ')])
    bool = BooleanField('allow')

@app.route('/',methods=['GET', 'POST'])
def index1():
    form = myform()
    if form.validate_on_submit():
        flash('บันทึกข้อมูลเรียบร้อย')
        session['name'] = form.text.data
        session['bool'] = form.bool.data
        session['gender'] = form.radio.data
        session['select'] = form.select.data
        session['address'] = form.textarea.data
        
        
        form.text.data = ''
        form.bool.data = ''
        form.radio.data = ''
        form.select.data = ''
        form.textarea.data = ''

    return render_template('boot_1.html',form=form)

@app.route('/boot_2.html',methods=['GET', 'POST'])
def index2():
    form = myform()
    if form.validate_on_submit():
        flash('บันทึกข้อมูลเรียบร้อย')
        session['name'] = form.text.data
        session['bool'] = form.bool.data
        session['gender'] = form.radio.data
        session['select'] = form.select.data
        session['address'] = form.textarea.data
        
        
        form.text.data = ''
        form.bool.data = ''
        form.radio.data = ''
        form.select.data = ''
        form.textarea.data = ''

    return render_template('boot_2.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)