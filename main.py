from flask import Flask, request, jsonify, render_template
import requests
from bs4 import BeautifulSoup
import os
import re

my_secret = os.environ['OPENAI_API_KEY']

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/scrape', methods=['POST'])
def scrape_url():
    url = request.json.get('url')
    if not url:
        return jsonify({'error': 'URL is required'}), 400
    
    # Scrape the URL
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    text = soup.get_text()
    text = re.sub(r'\s+', ' ', text)

    # Make a POST request to the OpenAI API
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {my_secret}"
    }
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "system", "content": "You are a summarizing assistant."},
            {"role": "user", "content": text}
        ]
    }
    response = requests.post(url, headers=headers, json=data)
    
    # Check the response status and send the completion in the response
    if response.status_code == 200:
        completion = response.json()['choices'][0]['message']['content']
        return jsonify({'success': True, 'result': completion}), 200
    else:
        return jsonify({'error': f"Request to OpenAI API failed with status {response.status_code}"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81)