from flask import Flask
import random

app = Flask(__name__)


@app.route('/')
def homepage():
    return "<h1>Guess a number between 0 and 9</h1>" \
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>"


@app.route('/<int:number>')
def check_number(number):
    if number == random_number:
        return "<h1 style='color: green'>You did it!</h1>" \
              "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>"
    elif number < random_number:
        return"<h1 style='color: red'>Too low. Try again.</h1>" \
              "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>"
    elif number > random_number:
        return "<h1 style='color: purple'>Too high. Try again.</h1>" \
              "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>"



random_number = random.randint(0, 9)

if __name__ == "__main__":
    app.run(debug=True)
