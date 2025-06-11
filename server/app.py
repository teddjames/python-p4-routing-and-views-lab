from flask import Flask, request, render_template_string

app = Flask(__name__)

# 1. Index view at `/`
@app.route("/")
def index():
    # Returns an <h1> with the title
    return "<h1>Python Operations with Flask Routing and Views</h1>"

# 2. print_string view at `/print/<string>`
@app.route("/print/<string:to_print>")
def print_string(to_print):
    # Print to console
    print(to_print)
    # Display in browser
    return to_print

# 3. count view at `/count/<int:n>`
@app.route("/count/<int:n>")
def count(n):
    # Join numbers 0..n-1 with newline, and add a final newline
    return "\n".join(str(i) for i in range(n)) + "\n"

# 4. math view at `/math/<int:a>/<op>/<int:b>`
@app.route("/math/<int:a>/<op>/<int:b>")
def math(a, op, b):
    # Choose operation
    if op == "+":
        result = a + b
    elif op == "-":
        result = a - b
    elif op == "*":
        result = a * b
    elif op == "div":
        # use integer division or float? adjust based on test expectations
        result = a / b
    elif op == "%":
        result = a % b
    else:
        return "Invalid operation", 400

    return str(result)


if __name__ == "__main__":
    # This allows `python app.py` to work without FLASK_APP
    app.run(port=5555, debug=True)
