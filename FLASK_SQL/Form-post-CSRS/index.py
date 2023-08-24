from flask import Flask,render_template,session
from flask_wtf import FlaskForm
from wtforms import StringField,\
    SubmitField,BooleanField,RadioField,SelectField,\
    TextAreaField

from wtforms.validators import DataRequired


app = Flask(__name__)
app.config['SECRET_KEY'] = 'mykey'

class MyForm(FlaskForm):
    # validators=[DataRequired] แจ้งเตือนให้ใส่ชื่อ
    name = StringField('ป้อนชื่อของคุณ',validators=[DataRequired])
    submit = SubmitField('save')
    bool = BooleanField('ยอมรับเงื่อนไขบริการข้อมูล')
    radio = RadioField('เพศ',choices=[('man','ชาย'),('girl','หญิง'),('other','อื่นๆ')])
    select = SelectField('ความสามารถ',choices=[('game','create game'),('website','create website'),('programer','programer'),('python','python')])
    textarea = TextAreaField('ที่อยู่')

@app.route('/',methods=['GET', 'POST'])
def index():
    form = MyForm()
    if form.validate_on_submit():
        session['name'] = form.name.data
        session['bool'] = form.bool.data
        session['gender'] = form.radio.data
        session['select'] = form.select.data
        session['address'] = form.textarea.data
        
        
        form.name.data = ''
        form.bool.data = ''
        form.radio.data = ''
        form.select.data = ''
        form.textarea.data = ''
    return render_template("index.html",form=form)

if __name__ == '__main__':
    app.run(debug=True)