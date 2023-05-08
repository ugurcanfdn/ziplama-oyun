from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return '''
        <form method="POST">
            <label>Enter first number:</label>
            <input type="number" name="num1"><br><br>
            <label>Enter second number:</label>
            <input type="number" name="num2"><br><br>
            <button type="submit" name="operation" value="add">Add</button>
            <button type="submit" name="operation" value="subtract">Subtract</button>
            <button type="submit" name="operation" value="multiply">Multiply</button>
            <button type="submit" name="operation" value="divide">Divide</button>
        </form>
    '''

@app.route('/', methods=['POST'])
def calculate():
    num1 = int(request.form['num1'])
    num2 = int(request.form['num2'])
    operation = request.form['operation']

    if operation == 'add':
        result = num1 + num2
    elif operation == 'subtract':
        result = num1 - num2
    elif operation == 'multiply':
        result = num1 * num2
    elif operation == 'divide':
        result = num1 / num2

    return f'<h1>Result: {result}</h1>'

if __name__ == '__main__':
     app.run(host= '0.0.0.0', port=80)
