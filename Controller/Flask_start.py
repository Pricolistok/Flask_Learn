from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    user = "Ученик Яндекс.Лицея"
    k = ['dhjd', 2, 4, 'ghjdo']
    print(k)
    return render_template('index.html', title='Домашняя страница',
                           ki = k)

if __name__ == '__main__':
    app.run(port=8000, host='127.0.0.1')