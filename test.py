from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return f'''
    <h2>Hello World</h2>
    '''

if __name__ == '__main__':
    app.run()