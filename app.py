from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/style.css')
def style():
    return render_template('style.css')

@app.route('/text_to_speech_project')
def text_to_speech():
    return render_template('text_to_speech.html')

if __name__ == '__main__':
    app.run(debug=True)
