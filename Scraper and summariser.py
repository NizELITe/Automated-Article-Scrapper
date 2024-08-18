from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
import nltk
import requests
from bs4 import BeautifulSoup
from flask import Flask, request, render_template, jsonify


nltk.download('punkt')

app = Flask(__name__)

def read_text_from_file(filename):
    with open(filename, 'r') as file:
        return file.read()
# Input text to be summarized



def fetch_page_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for non-200 status codes
        soup = BeautifulSoup(response.content, 'html.parser')
        return soup.get_text()
    except requests.exceptions.RequestException as e:
       
        return None


@app.route('/summarize', methods=['POST'])
def summarize():
    data = request.json
    url = data.get('url')
    content = fetch_page_content(url)

    if content:
        # Parse the content and summarize it
        parser = PlaintextParser.from_string(content, Tokenizer("english"))
        summarizer = LsaSummarizer()
        summary_sentences = summarizer(parser.document, sentences_count=5)  # Adjust the number of sentences as needed
        summary = ' '.join(map(str, summary_sentences))  # Convert the summary sentences to a single string
        return jsonify({'summary': summary})
    else:
        return jsonify({'error': 'Failed to fetch content or no content found'}), 400

if __name__ == '__main__':
    app.run(debug=True)


