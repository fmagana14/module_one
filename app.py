from flask import Flask
import random 


app = Flask(__name__)

# Whats your favorite animal
@app.route('/')
def homepage():
    return 'Whats your favorite animal?'

@app.route('/animal/<user_animal>')
def favorite_animal(user_animal):
    return f"Wow, {user_animal} is my favorite animal, too!"

# users favorit dessert
@app.route('/dessert/<user_dessert>')
def favorite_dessert(user_dessert):
    return f"How did you know I liked {user_dessert}?"

# Multiply two numbers!
@app.route('/multiply/<number1>/<number2>')
def multiply(number1, number2):
    if number1.isdigit() and number2.isdigit():
        number1 = int(number1)
        number2 = int(number2)

        results = number1 * number2
        return f"{number1} times {number2} is {results}"
    else:
        return "Invalid inputs. Please try again by entering 2 numbers!"

# Say n times
@app.route('/sayntimes/<word>/<int:n>')
def sayntimes(word, n):
    if isinstance(word, str) and isinstance(n, int) and n > 0:
        repeated_word =' '.join([word] * n)
        return repeated_word
    else:
        return "Invalid input. Please try again by entering a word and a positive integer!"
if __name__ == '__main__':
    app.run(debug=True)