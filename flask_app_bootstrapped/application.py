from flask import Flask, render_template, request, flash
from recommender import random_recommender

app = Flask(__name__)
app.secret_key = b'need_this_for_message_flashing'

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/recommender')
def recommender():
    return render_template('recommender.html')

@app.route('/results')
def results():
    user_input = request.args #some kind of dictionary-like object

    movie_list = random_recommender(6, user_input)

    if user_input['pun'] == 'Yes':
        message = "Great! You're gonna love these recommendations!"
        status = "pun-success"
    else:
        message = "Wow, your life is boring. Try watching these films."
        status = "pun-failure"

    flash(message)

    return render_template('results.html', movies=movie_list, status=status)
