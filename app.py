from flask import Flask, render_template, request, send_file
import requests
import json

app = Flask(__name__)

# Замените это значение на ваш реальный ключ API
PROXY_API_KEY = 'your_proxy_api_key'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_article():
    input_text = request.form['inputText']
    response = requests.post(
        'https://api.proxyapi.ru/openai/v1/chat/completions',
        headers={
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {PROXY_API_KEY}'
        },
        data=json.dumps({
            "model": "gpt-4o-mini",
            "messages": [{"role": "user", "content": input_text}]
        })
    )
    data = response.json()
    generated_text = data['choices'][0]['message']['content']
    return {'generatedText': generated_text}

@app.route('/download', methods=['POST'])
def download_article():
    output_text = request.form['outputText']
    with open('generated_article.txt', 'w') as file:
        file.write(output_text)
    return send_file('generated_article.txt', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
