from flask import Flask

app = Flask(__name__)

@app.route('/')
def homepage():
    return 'Whats your favorite animal?'

@app.route('/animal/<user_animal>')
def favorite_animal(user_animal):
    return f"Wow, {user_animal} is my favorite animal, too!"

@app.route('/dessert/<user_dessert>')
def favorite_dessert(user_dessert):
    return f"How did you know I liked {user_dessert}?"

@app.route('/multiply/<number1>/<number2>')
def multiply(number1, number2):
    if number1.isdigit() and number2.isdigit():
        number1 = int(number1)
        number2 = int(number2)

        results = number1 * number2
        return f"{number1} times {number2} is {results}"
    else:
        return "Invalid inputs. Please try again by entering 2 numbers!"




if __name__ == '__main__':
    app.run(debug=True)