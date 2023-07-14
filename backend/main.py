from flask import Flask, jsonify, request
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

GAMES = [

    {   
        # 'id': uuid.uuid4().hex,
        'title':'2k21',
        'genre':'sports',
        'played': True,
    },
    {   
        # 'id': uuid.uuid4().hex,
        'title':'Evil Within',
        'genre':'horror',
        'played': False,
    },
    {   
        # 'id': uuid.uuid4().hex,
        'title':'the last of us',
        'genre':'survival',
        'played': True,
    },
    {  
        # 'id': uuid.uuid4().hex,
        'title':'days gone',
        'genre':'horror/survival',
        'played': False,
    },
    {   
        # 'id': uuid.uuid4().hex,
        'title':'mario',
        'genre':'retro',
        'played': True,
    }

]

# frontend와 연결
@app.route('/games', methods=['GET', 'POST'])
def all_games():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        GAMES.append({
            'title': post_data.get('title'),
            'genre': post_data.get('genre'),
            'played': post_data.get('played'),
        })
        response_object['message'] = 'Game Added!'
    else:
        response_object['games'] = GAMES
    return jsonify(response_object)


if __name__ == "__main__":
    app.run(debug=True)