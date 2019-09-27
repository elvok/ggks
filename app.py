from flask import Flask,json,render_template

app = Flask(__name__)


@app.route('/',methods=['GET'])
def index():
    # 返回一个页面
    server = getFile()
    host = server["host"]
    return render_template("index.html", host=host)

def getFile():
    f = open('server.json', encoding='utf-8')
    return json.load(f)
if __name__ == '__main__':
    app.run()
