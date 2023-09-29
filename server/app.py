#!/usr/bin/env python3
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, make_response, jsonify, session
from flask_migrate import Migrate

from models import db, Article, User

app = Flask(__name__)
app.secret_key = b'Y\xf1Xz\x00\xad|eQ\x80t \xca\x1a\x10K'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/clear')
def clear_session():
    session['page_views'] = 0
    return {'message': '200: Successfully cleared session data.'}, 200

@app.route('/articles')
def index_articles():

    pass

@app.route('/articles/<int:id>')
def show_article(id):

    pass

@app.route('/articles/<int:id>', methods=['GET'])
def show_article_details(id):
    #check if 'page_views' is in the session, if not, set it to 0
    session['page_views'] = session.get('page_views', 0)

    #increment the 'page_views' count  for each request
    session['page_views'] += 1
    print(f"page_views: {session['page_views']}")

    #check if the user has viewd more than 3 pages
    if session['page_views'] > 3 :
        #Return an unauthorized(401) response
        return jsonify({'message': 'Maximum pageview limit reached '}), 401
    
    #if the user has viewd 3 or fewer pages, return the articles data(replace this with your actual data)
    article_data = {
        'id': id,
        'title': 'sample Article',
        'content': 'This is a sample article content.'
 }
    # Return a valid response with status code 200 (OK)
    return jsonify({'article': article_data}), 200
    
    
    return jsonify({'article': article_data, 'page_views': session['page_views']})





if __name__ == '__main__':
    app.run(port=5555)
