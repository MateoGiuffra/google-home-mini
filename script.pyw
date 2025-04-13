from flask import Flask, request
import webbrowser
import threading

app = Flask(__name__)

@app.route('/abrir', methods=['GET'])
def abrir_youtube():
    url = request.args.get('url', 'https://youtube.com')
    threading.Thread(target=webbrowser.open, args=(url,)).start()
    return f'Abriendo {url}', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
