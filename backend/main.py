from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__) # 응용 프로그램 인스턴스화(?)
app.config.from_object(__name__) # 응용 프로그램 지속적으로 업데이트 할수 잇게 해준다함

CORS(app, resources={r"/*": {'origins': '*'}})
# CORS(app, resources={r"/*": {'origins': 'https://localhost:8080', 'allow_headers': 'Access-Control-Allow_Origin'}})

# hello world route
@app.route('/', methods=['GET'])
def greetings():
    return ('Hello, world!')

# frontend와 연결
@app.route('/shark', methods=['GET'])
def shark():
    return ('Shark🦈!!')

if __name__ == "__main__":
    app.run(debug=True)