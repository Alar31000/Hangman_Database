from flask import Flask, request, jsonify, Response
from flask_sqlalchemy import SQLAlchemy
import simplejson as json
import enum

# localhost:3306

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:Michelicious11!@localhost:3306/hangman'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

hdb = SQLAlchemy(app)


@app.route('/')
def hello_world():
    """Print 'Hello, world!' as the response body."""
    return 'Hello, caca!'


@app.route('/test')
def testing():
    """Print 'Hello, world!' as the response body."""
    return 'test!'


@app.route('/words', methods=['POST'])
def words():
    # words_id = request.form.get('words_id')
    mot = request.form.get('mot')
    difficulte = request.form.get('difficulte')
    save_to_db(mot, difficulte)
    return "it worked"


class Words(hdb.Model):
    id = hdb.Column(hdb.Integer, primary_key=True)
    mot = hdb.Column(hdb.String(20), unique=True, nullable=False)
    difficulte = hdb.Column(hdb.Enum, unique=True, nullable=False)



def save_to_db(mot, difficulte):
    word_to_add = Words(mot=mot, difficulte=difficulte)
    hdb.session.add(word_to_add)
    hdb.session.commit()



if __name__ == "__main__":
    app.run(host='0.0.0.0', debug= True, port=3310)