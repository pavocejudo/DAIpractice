from flask import Flask
from flask import request
from flask import render_template
import re
from mandelbrot import *
app = Flask(__name__)

def valid_login(x,y,x2,y2,w):
    if (x>0) and (x<1):
        if (y>0) and (y<1):
            if (x2>0) and (x2<1):
                if (y2>0) and (y2<1):
                    if w>0:
                        return True
    return False

@app.route('/mandelbrot',methods=['POST','GET'])
def mandelbrot():
    if request.method == 'POST':
        x = float(request.form['valor_x'])
        y=float(request.form['valor_y'])
        x2=float(request.form['valor_x2'])
        y2=float(request.form['valor_y2'])
        width=int(request.form['width'])
        print x,y,x2,y2,width
        print valid_login(x,y,x2,y2,width)
        if valid_login(x,y,x2,y2,width):
            renderizaMandelbrot(x,y,x2,y2,width,100,'static/img-mandelbrot.png')
            return render_template('imagen-mandelbrot.html')
        return render_template('mandelbrot.html')

@app.route('/mandelbrotBonito',methods=['POST','GET'])
def mandelbrotBonito():
    if request.method == 'POST':
        x = float(request.form['valor_x'])
        y=float(request.form['valor_y'])
        x2=float(request.form['valor_x2'])
        y2=float(request.form['valor_y2'])
        width=int(request.form['width'])
        #[(100,100,100),(210,034,123)]



        color = []
        paleta = re.findall('(\d)',request.form['paleta'])
        for i in range(len(paleta)):
            if i%3==0 and i!=0:
                paleta.append(tuple(color))
                color = []
            color.append(int(paleta[i]))
            print color


        nColores = int(request.form['nColores'])
        if valid_login(x,y,x2,y2,width):
            renderizaMandelbrotBonito(x,y,x2,y2,width,100,'static/img-mandelbrot.png',paleta,nColores)
            return render_template('imagen-mandelbrot.html')
        return render_template('mandelbrot.html')


@app.route('/')
def renderizar():
    return render_template('mandelbrot.html')

if __name__=="__main__":
    app.run(debug=True)
