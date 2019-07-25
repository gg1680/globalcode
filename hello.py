from flask import Flask, render_template, request

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

@app.route('/handle_data', methods=['POST'])
def handle_data():
    n = request.form['name']
    return render_template('name.html', to=n)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
