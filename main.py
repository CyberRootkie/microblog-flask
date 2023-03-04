from flask import Flask, render_template, Response
from markupsafe import escape
import os

# TODO
# Index --> lister les articles et les rendres cliquables
# Post via markdown
# Moteur de recherche

app = Flask(__name__)

def getAllPosts():
    list_posts = []
    for file in os.scandir('./posts/'):
        if file.is_file:
            slug = file.name.replace('.txt', '')
            list_posts.append(slug)
    print(list_posts)

def getPost(slug):
    f = open(f"./posts/{slug}.txt", 'r')
    content = f.read()
    f.close()
    return content

@app.route("/")
def index():
    list_posts = getAllPosts()
    title = "Title"
    body = "Hello World !"
    return render_template("index.html", title=title, body=body, posts=list_posts)

@app.route("/post/<slug>.htm")
def post(slug):
    slug = escape(slug)
    content = getPost(slug)
    return(content)


@app.route("/robots.txt")
def robotstxt():
    content = "User-Agent:*\nDisallow:"
    return Response(content, mimetype='text/plain')

app.run(host="0.0.0.0", port=9876)



