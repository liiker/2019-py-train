from flask import Flask, request, redirect
from flask import render_template
import mysql.connector

app = Flask(__name__)

conn = mysql.connector.connect(
    user='homestead', password='secret',
    database='homestead',
    use_unicode=True, port=33060)


def query(conn, sql, params=[]):
    cursor = conn.cursor(dictionary=True)
    cursor.execute(sql, params)
    rows = cursor.fetchall()
    cursor.close()
    return rows


def execute(conn, sql, params=[]):
    cursor = conn.cursor()
    cursor.execute(sql, params)
    conn.commit()
    cursor.close()
    return cursor.rowcount


@app.route("/")
def hello():
    return '<span class="box">Hello World!!!!</span><link rel="stylesheet" href="/static/css/index.css" /><img style="width:100px" src="/static/image/python.jpg"/><script src="/static/js/index.js"></script>'


@app.route('/posts')
def post():
    posts = query(conn, 'select * from xposts order by id desc')
    print(posts)
    return render_template('index.html', posts=posts)


@app.route('/post/send')
def send_post():
    return render_template('send_post.html')


@app.route('/post/save', methods=['POST'])
def save_post():
    p = request.form

    sql = 'insert into xposts (title, author, image, content, publish_at) values (%s, %s, %s, %s, now())'
    result = execute(conn, sql, [p.get('title'),
                                 p.get('author'),
                                 p.get('image'),
                                 p.get('content'),
                                 ])
    if result == 1:
        return redirect('/posts')
    else:
        return 'save error!'
