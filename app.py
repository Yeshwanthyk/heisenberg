from flask import Flask
from .helpers import parsed_quotes

app = Flask(__name__)

@route('/random')
def random_quotes():
    quotes = parsed_quotes()
    return render_template(random_quote.html, quotes=quotes)

