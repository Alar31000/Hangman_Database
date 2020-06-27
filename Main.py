from flask import Flask, request, jsonify, Response
from flask_sqlalchemy import SQLAlchemy
import simplejson as json

# localhost:3306

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqldb://root:Hurricaner2!@localhost[:3306]/db_hangman'
db = SQLAlchemy(app)

hangman_db = SQLAlchemy(app)


@app.route('/')
def hello_world():
    """Print 'Hello, world!' as the response body."""
    return 'Hello, world!'


@app.route('/words', methods=["POST"])
def add_word():
    words_id = request.form.get('words_id')
    mot = request.form.get('mot')
    difficulte = request.form.get('difficulte')
    hangman_db.session.add(words)
    save_to_db(mot, difficulte)
    return ""


class Word(db_hangman.Model):
    id = db_hangman.Column(db_hangman.Integer, primary_key=True)
    mot = db_hangman.Column(db_hangman.String(20), unique=True, nullable=False)
    difficulte = db_hangman.Column(db_hangman.String(255), unique=True, nullable=False)


def save_to_db(mot, difficulte):
    word_to_add = Word(mot=mot, difficulte=difficulte)
    dbsession.add(word_to_add)
    session.commit()
    return jsonify(Word=word_to_add.serialize)