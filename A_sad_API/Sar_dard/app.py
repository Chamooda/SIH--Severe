from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/urls/<string:urls>')
def urls_playboy(urls):
    urls = urls.replace(' ','/')
    return jsonify({
        'status': 'ok',
        'message': 'Hello World!',
        'urls': urls})
    

@app.route('/justcheckin')
def justcheckin():
    return jsonify({
        'status': 'ok',
        'message': 'Hello World!',
        'brocode': '200'})
@app.route('/')
def index():
    return "ok"


if __name__ == '__main__':
    app.run(debug=True)
