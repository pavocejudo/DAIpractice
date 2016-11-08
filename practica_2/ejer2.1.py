from flask import Flask
from flask import url_for, render_template
app = Flask(__name__)

@app.route('/')
def web():
    return render_template('hello.html')

if __name__ == "__main__":
  app.run(debug = True, host='0.0.0.0')
