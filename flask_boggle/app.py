from boggle import Boggle
from flask import Flask,render_template


boggle_game = Boggle()

app = Flask(__name__)

@app.route('/')
def start_page():
    return render_template('start.html')

@app.route('/start')
def boggle_page():
    make_board = boggle_game.make_board()
    return render_template('table.html',board = make_board)
