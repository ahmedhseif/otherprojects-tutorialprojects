from flask import Flask


def make_bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"
    return wrapper

def make_emphasis(function):
    def wrapper():
        return "<em>" + function() + "</em>"
    return wrapper

def make_underlined(function):
    def wrapper():
        return "<u>" + function() + "</u>"
    return wrapper


app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1 style="text-align: center">Hello, World!</h1>' \
           '<p>This is a paragraph.</p>' \
           '<img src="https://i.giphy.com/media/njtPBlbYnHAHK/giphy.webp" height=200 width=200>'


@app.route('/bye')
@make_bold
def say_bye():
    return "Bye"

# @make_emphasis
# @make_underline


@app.route('/username/<name>/<int:number>')
def greeting(name, number):
    return (f"Hello there, {name}, you are {number} years old")


if __name__ == "__main__":
    app.run(debug=True)
