from flask import Flask,render_template
from newsapi import NewsApiClient


app = Flask(__name__)


@app.route('/')

def Index():
    newsapi = NewsApiClient(api_key="5007f22fe7cf4cf09e43bae096991b2d")
    topheadlines = newsapi.get_top_headlines(sources="abc-news")

    articles = topheadlines['articles']

    desc = []
    news = []
    img = []

    for i in range(len(articles)):
        myarticles = [articles[i]]


        news.append(myarticles['title'])
        desc.appen(myarticles['description'])
        img.append(yarticles['urlToImage'])
    
    mylist = zip(news,desc,img)

    return render_template('index.html', context = mylist)


if __name__=="__main__":
    app.run(debug=True)