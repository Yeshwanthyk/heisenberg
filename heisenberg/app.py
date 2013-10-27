from flask import Flask, render_template
from helpers import parse_quotes

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/random')
def random_quotes():
    quotes = parse_quotes()
    return render_template('random_quote.html',quotes = quotes)

if __name__ == '__main__':
    app.run(debug=True)
