 #!/usr/bin/python
 # -*- coding: UTF-8 -*-



from flask import Flask, session, redirect, url_for, escape, request
import urllib
from flask import render_template
import re
from users import Users
from wtforms import Form, BooleanField, TextField, PasswordField, validators, SelectField, DateField, TextAreaField, RadioField, ValidationError
import anydbm #Modulo para base de datos dbm
from pymongo import MongoClient


import sys
reload(sys)
sys.setdefaultencoding('utf-8')

app = Flask(__name__)

#conexion a la base de datos dbm
db = anydbm.open('datos.dat','c')
mongoClient = MongoClient('localhost',27017)
if mongoClient:
    print "Conectado a la base de datos"
mb = mongoClient.UserDB
if mb:
    print "conexion establecida"
collection = mb.UserTable
if collection:
    print "Tablas creadas"

#Identificar correos electronicos validos
def IdentificarCorreos(correo):
    match = bool(re.match('(\w+)@((\w+)\.)+(\w+)',correo))
    return match

#Identificar numeros de tarjeta de credito validos separados por espacio o '-'
def IdentificarTarjetasDeCredito(form, field):
    match = bool(re.match('(\d{4}( |-)){3}(\d{4})', field.data))
    if match == False:
        raise ValidationError('VISA number not valid, please insert with the format XXXX-XXXX-XXXX-XXXX')


class RegistrationForm(Form):
    days = []
    for i in range(1,32):
        a = ("\'"+str(i)+"\'",i)
        days.append(a)

    month = []
    for i in range(1,13):
        a = ("\'"+str(i)+"\'",i)
        month.append(a)

    year = []
    for i in range(1900,2017):
        a = ("\'"+str(i)+"\'",i)
        year.append(a)

    username = TextField('',[ validators.InputRequired(),validators.Length(min=4, max=25)])
    second_name= TextField( '',[validators.Length(min=4, max=50),validators.InputRequired()])
    email = TextField('', [validators.InputRequired(),validators.Email('This email format is not valid')])
    pay = RadioField('',choices = [('VISA','VISA'),('COD','COD')])
    VISA= TextField('', [validators.Length(min=4, max=25),validators.InputRequired(), IdentificarTarjetasDeCredito])
    birthday  = SelectField('Day: ', choices=days)
    birthmoth = SelectField('Month: ', choices=month)
    birthyear = SelectField('Year: ', choices=year)
    adress = TextAreaField('',[validators.InputRequired()])
    password = PasswordField('', [
        validators.Required(),
        validators.EqualTo('confirm', message='La contrasenia debe coincidir con la repeticion'),validators.InputRequired(),
        validators.Length(min=7)])
    confirm = PasswordField('')
    accept_tos = BooleanField('Acepto las condiciones', [validators.Required('This box must be checked'),validators.InputRequired()])



@app.route('/')
def view():
    #if 'username' in session:
        #session['inDB']=session['username'] in db;
    return render_template('index.html')

@app.before_request
def historial():
    if 'historial' in session:
        session['historial'].append(request.url)
        if len(session['historial']) > 3:
            session['historial'].pop(0)


@app.route('/')
def index():
    if 'username' in session:
        resp = make_response()
        resp.set_cookie('username', 'the username')
        return 'Logged in as %s' % escape(session['username'])
    return 'You are not logged in'

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        log = collection.find_one({"name":request.form.get('username',None)})
        if log['password'] == request.form.get('password',None) :
            print "----------------------- Encontrado -------------------------"
            print log['name']
            print log['password']
            session['username'] = request.form['username']
            session['historial'] = []
            return redirect(url_for('index'))
        return render_template('index.html')
    return render_template('index.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/modify', methods = ['GET', 'POST'])
def modify():
    form = RegistrationForm(request.form)
    db = anydbm.open('datos.dat','c')
    datos = db[session['username']].split(",")
    db.close()

    if request.method == 'POST':
        #db = anydbm.open('datos.dat', 'c')
        #db[form.username.data] = str(form.username.data) +","+ str(form.second_name.data) +","+ str(form.email.data) +","+ str(form.birthday.data)+","+str(form.birthmoth.data)+","+str(form.birthyear.data) +","+ str(form.pay.data) +","+ str(form.VISA.data) +"," + str(form.password.data)
        #db.close()
        collection.update_one({'name':session['username']},{"$set":{"name":form.username.data,"second_name":form.second_name.data, "email":form.email.data,'pay':form.pay.data,'VISA':form.VISA.data,'adress':form.adress.data,'birthday':form.birthday.data,'birthmoth':form.birthmoth.data,'birthyear':form.birthyear.data}})
        if form.password.data != "":
            collection.update_one({'name':session['username']},{"$set":{'password':form.password.data}})
        return redirect(url_for('index'))

    log = collection.find_one({"name":session['username']})

    form.username.data = log['name']
    form.second_name.data = log['second_name']
    form.email.data = log['email']
    form.adress.data = log['adress']
    form.pay.data = log['pay']
    form.VISA.data = log['VISA']
    form.birthday.data = log['birthday']
    form.birthmoth.data = log['birthmoth']
    form.birthyear.data = log['birthyear']
    form.password.data = log['password']

    #form.username.data = datos[0]
    #form.second_name.data = datos[1]
    #form.email.data = datos[2]
    #form.pay.data = datos[6]
    #form.VISA.data = datos[5]

    return render_template('modify.html', user_data=datos, form=form)


@app.route('/register', methods = ['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)

    if request.method == 'POST' and form.validate():
        username = str(form.username.data)
        second = str(form.second_name.data)
        email = str(form.email.data)
        adress = str(form.adress.data)
        day = str(form.birthday.data)
        month = str(form.birthmoth.data)
        year = str(form.birthyear.data)
        method_pay=str(form.pay.data)
        nVisa= str(form.VISA.data)
        passw = str(form.password.data)
        #user = Users(str(form.username.data),str(form.second_name.data),str(form.email.data),str(form.birthday.data),str(form.birthmoth.data),str(form.birthyear.data),str(form.pay.data),str(form.VISA.data),str(form.password.data))

        newUser = {"name":username,
            "second_name":second,
            "email":email,
            "adress":adress,
            "birthday":day,
            "birthmoth":month,
            "birthyear":year,
            "pay":method_pay,
            "VISA":nVisa,
            "password":passw}
        #db[form.username.data] = str(form.username.data) +","+ str(form.second_name.data) +","+ str(form.email.data) +","+ str(form.birthday.data)+","+str(form.birthmoth.data)+","+str(form.birthyear.data) +","+ str(form.pay.data) +","+ str(form.VISA.data) +"," + str(form.password.data)
        posted = collection.insert(newUser)
        if posted:
            print "Usuario aniadido"
        return redirect(url_for('index'))

    return render_template('register.html', form=form)

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))

# set the secret key.  keep this really secret:
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'



if __name__ == '__main__':
    app.run(debug=True, port=5000)
