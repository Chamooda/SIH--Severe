from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/urls/<string:urls>')
def urls_playboy(urls):
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



if __name__ == '__main__':
    app.run(debug=True)