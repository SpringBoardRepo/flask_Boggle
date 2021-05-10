from boggle import Boggle
from flask import Flask,render_template, request, session, jsonify


boggle_game = Boggle()

app = Flask(__name__)
app.config['SECRET_KEY'] = 'boggle_secret'

@app.route('/')
def start_page():
    return render_template('start.html')

@app.route('/start')
def boggle_page():
    make_board = boggle_game.make_board()
    session['board'] = make_board
    high_score = session.get('high_score',0)
    nplays = session.get('nplays',0)
    return render_template('index.html',board = make_board ,high_score=high_score,nplays=nplays)

@app.route('/check-word')
def check_word():
    word  = request.args['word']
    board = session['board']
    response = boggle_game.check_valid_word(board,word)

    return jsonify({'result' : response})

@app.route('/post-score', methods = ['POST'])
def post_score():

    score = request.json['score']
    highscore = session.get('highscore',0)
    nplays = session.get('nplays',0)

    session['nplays'] = nplays+1
    session['highscore'] = max(score,highscore)

    return jsonify(brokerecord=score>highscore)
