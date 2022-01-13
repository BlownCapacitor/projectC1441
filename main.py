from flask import Flask, jsonify, request
import csv

all_articles = []
liked_articles = []
disliked_articles = []
not_read_articles = []

with open('Articles.csv', encoding="utf8") as f:
    reader = csv.reader(f)
    data = list(reader)
    all_articles = data[1:]

app = Flask(__name__)

@app.route("/allArticles")

def allArticles():
    return jsonify({
        "data" : all_articles[0],
        "status" : "All Articles"
    }),000

@app.route("/likedArticles", methods = ["POST"])

def likedArticles():
    global all_articles
    article2 = all_articles[0]
    all_articles = all_articles[1:]
    liked_articles.append(article2)
    return jsonify({
      "message" : "Liked articles"
    }),100

@app.route("/dislikedArticles", methods = ["POST"])

def dislikedArticles():
    global all_articles
    article3 = all_articles[0]
    all_articles = all_articles[1:]
    disliked_articles.append(article3)
    return jsonify({
        "Message" : "Disliked articles"
    }),200

@app.route("/didNotRead", methods = ["POST"])

def didNotWatch():
    global all_articles
    article4 = all_articles[0]
    all_articles = all_articles[1:]
    didNotWatch.append(article4)
    return jsonify({
        "message" : "Did Not Read"
    }),300
if __name__ == "__main__":
    app.run()