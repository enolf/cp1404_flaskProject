from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return '<h1>Hello World :)</h1'


@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return f"Hello {name}"


@app.route('/c2f/<input_temp>')
def web_print_c2f(input_temp=''):
    return f"{c_to_fahrenheit(float(input_temp))}"


def c_to_fahrenheit(convert):
    """Convert Celsius to Fahrenheit"""
    fahrenheit = convert * 9.0 / 5 + 32
    return fahrenheit


if __name__ == '__main__':
    app.run()
