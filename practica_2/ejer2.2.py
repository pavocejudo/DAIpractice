from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/user/<username>")
def mostrarPerfilusuario(username):
    return 'Usuario %s' % username

@app.route('/user/')
def mostrarConParametros(username=None):
    parametro1= request.args.get('par1')
    parametro2= request.args.get('par2')
    return parametro1 +' '+ parametro2


@app.errorhandler(404)
def page_not_found(error):
    return "La pagina no existe",404

if __name__=="__main__":
    app.run(debug=True)
