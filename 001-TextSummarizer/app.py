from flask import Flask
from flask import render_template
from flask import request
import nltk
nltk.download('punkt')


app = Flask(__name__)

def index():
    return render_template('index.html') 

def summarize_text(text):
    sentences = nltk.sent_tokenize(text) # tokenize sentences into NLTK
    summary = sentences[0]
    for sentence in sentences[1:]:  # concatenate first 5 sentences into summary
        summary += " " + sentence
    # if summary > 500 chars, truncate it + add ellipsis
    summary = summary[:500] + "..." if len(summary)>500 else summary
    return summary

@app.route('/summarize', methods=['POST'])

def summarize():
    text = request.form['text'] # recieve text input from form
    summary = summarize_text(text) # generate summary
    return render_template('summary.html', summary=summary) # render



def handle_exception(err):
  path = request.path # this var was shown to be 'favicon.ico' or 'manifest.json'


def main():
    return index()

if __name__ == "__main__":
    app.run()