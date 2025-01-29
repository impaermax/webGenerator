document.getElementById('generateButton').addEventListener('click', generateArticle);
document.getElementById('downloadButton').addEventListener('click', downloadArticle);

async function generateArticle() {
    const inputText = document.getElementById('inputArea').value;
    const response = await fetch('/generate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ inputText })
    });

    const data = await response.json();
    document.getElementById('outputArea').value = data.generatedText;
}

async function downloadArticle() {
    const outputText = document.getElementById('outputArea').value;
    await fetch('/download', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ outputText })
    }).then(response => response.blob())
      .then(blob => {
          const url = window.URL.createObjectURL(blob);
          const a = document.createElement('a');
          a.href = url;
          a.download = 'generated_article.txt';
          document.body.appendChild(a);
          a.click();
          a.remove();
          window.URL.revokeObjectURL(url);
      });
}
