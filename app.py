from flask import Flask,jsonify,request

from storage import all_articles, liked_articles, unliked_articles, unseen_articles
from demographic_filtering import output
from content_based_filtering import get_recommendations




app = Flask(__name__)

@app.route('/get_article')

def get_article():
    return jsonify({
        "data": all_articles[0],
        "status": "success"
    }), 200

@app.route('/liked_article', methods=["POST"])

def liked_article():
    article = all_articles[0]
    all_articles = all_articles[1:]
    liked_articles.append(article)
    return jsonify({
        "status": "success"
    }), 201

@app.route('/unliked_article', methods=["POST"])

def unliked_article():
    article = all_articles[0]
    all_articles = all_articles[1:]
    unliked_articles.append(article)
    return jsonify({
        "status": "success"
    }), 202

@app.route('/unseen_article', methods=["POST"])

def unseen_article():
    article = all_articles[0]
    all_articles = all_articles[1:]
    unseen_articles.append(article)
    return jsonify({
        "status": "success"
    }), 201

@app.route("/popular-articles")
def popular_articles():
    article_data = []
    for article in output:
        _d = {
            "title": article[11],
            "text": article[12],
        }
        article_data.append(_d)
    return jsonify({
        "data": article_data,
        "status": "success"
    }), 200

@app.route("/recommended-articles")
def recommended_articles():
    all_recommended = []
    for liked_article in liked_articles:
        output = get_recommendations(liked_article[19])
        for data in output:
            all_recommended.append(data)
    import itertools
    all_recommended.sort()
    all_recommended = list(all_recommended for all_recommended,_ in itertools.groupby(all_recommended))
    article_data = []
    for recommended in all_recommended:
        _d = {
            "title": recommended[11],
            "text": recommended[12],
        }
        article_data.append(_d)
    return jsonify({
        "data": article_data,
        "status": "success"
    }), 200




if __name__ =="__main__":
    app.run()

