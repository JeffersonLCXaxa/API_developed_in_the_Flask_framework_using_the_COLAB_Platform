pip install flask

from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/index')
def index():
    data = {
        "Number": [1, 2, 3, 4, 5],
        "Name": ["Mahesh", "Alex", "David", "John", "Chris"],
        "Age": [25, 26, 27, 28, 29],
        "Country": ["India", "UK", "USA", "Canada", "France"]
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run()
