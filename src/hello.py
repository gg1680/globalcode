from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/whereami')
def whereami():
    return 'Ghana!'

@app.route('/foo/<name>')
def foo(name):
    return render_template('name.html', to=name)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
