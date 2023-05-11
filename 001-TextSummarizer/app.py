from flask import Flask, render_template, request
import nltk


app = Flask(__name__)

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

@app.errorhandler(404)
def not_found(e):
  return render_template("404.html")


def handle_exception(err):
  path = request.path # this var was shown to be 'favicon.ico' or 'manifest.json'