from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/random-number')
def random_number():
    number = random.randint(1, 100)
    return f'<p>Your random number is: {number}</p>'

if __name__ == '__main__':
    app.run(debug=True)
