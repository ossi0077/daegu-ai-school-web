#flask를 배워보자
#application server(웹서버가 아니라 앱서버라고 보통 한다)
#app.run()으로 실행시키는데 코드를 보니 한줄만 들어가면 되는듯.
from flask import Flask
import random as rd

app = Flask(__name__)

# topics의 body 딕셔너리를 없애고 /read/<int:id> 페이지에 반복문으로 추가시켜 놓았다.
topics = [
  {"id":1, "title":"html"},
  {"id":2, "title":"css"},
  {"id":3, "title":"javascript"}
]

def template(content):
    liTags = ''
    for topic in topics:
        liTags = liTags + f"<li><a href='/read/{topic['id']}/'>{topic['title']}</a></li>"
    return f'''
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset='utf-8'>
        
    </head>
    <body>
        <h1><a href="/">WEB</a></h1>
        <ol>
            {liTags}
        </ol>
        {content}
        <ul>
        <li><a href="/create/">create</a></li>
        </ul>
    </body>
    </html>
    '''

@app.route("/")
def index():
    return template('<h2>Welcome</h2>Hello, WEB!')

@app.route("/read/<int:id>/")
def read(id):
    title = ''
    body = ''
    for topic in topics :
        if topic['id'] == id:
            title = topic['title']
            body = f"{topic['title']} is ...."
            break;
    return template(f'<h2>{title}</h2>{body}')

#input, area 등의 부모태그는 form 태그이다.
#form 태그는 action으로 안의 내용을 전송한다.
#name="q"를 하면 q이름이 붙여서 전송한다.
@app.route('/create/')
def create():
    content='''
        <form action="/create/">
            <p><input type="text" name="title" placeholder="title"></p>
            <p><textarea name="body" placeholder="body"></textarea></p>
            <p><input type="submit" value="create"></p>
        </form>
    '''
    return template(content)

@app.route('/update/')
def update():
  return 'Update'

app.run()