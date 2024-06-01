
<h1>Porsche Chatbot API</h1>

<h2>Overview</h2>

<p>The Porsche Chatbot API is a powerful tool for integrating a chatbot with speech-to-text and text-to-speech functionality into Porsche-related applications. This API provides a seamless interface for interacting with the chatbot and leveraging cutting-edge language models for natural language processing.</p>

<h2>Features</h2>

<ul>
    <li><strong>Chatbot Integration:</strong> Easily integrate a chatbot into your Porsche-related applications.</li>
    <li><strong>Speech-to-Text:</strong> Convert spoken input into text for processing by the chatbot.</li>
    <li><strong>Text-to-Speech:</strong> Convert text responses from the chatbot into spoken audio.</li>
    <li><strong>Language Model Interaction:</strong> Access state-of-the-art language models for advanced natural language understanding.</li>
    <li><strong>Web Scraping:</strong> Optional functionality for scraping data from the web to enhance the chatbot's capabilities.</li>
</ul>

<h2>Getting Started</h2>

<h3>Installation</h3>

<ol>
    <li>Clone the repository:</li>
    <pre><code>git clone https://github.com/yourusername/porsche-chatbot-api.git</code></pre>
    <li>Navigate to the project directory:</li>
    <pre><code>cd porsche-chatbot-api</code></pre>
    <li>Install dependencies:</li>
    <pre><code>pip install -r requirements.txt</code></pre>
</ol>

<h3>Configuration</h3>

<p>Set up environment variables by creating a <code>.env</code> file in the project root directory and populating it with your configuration:</p>

<pre><code>
    Add your OpenAI key as environment var should be named as: OPENAI_API_KEY
</code></pre>

<h3>Usage</h3>

<ol>
    <li>Start the Flask server:</li>
    <pre><code>python api/api.py</code></pre>
    <li>Access the API endpoints using tools like <code>curl</code>, <code>Postman</code>, or by integrating with your application.</li>
</ol>

<h3>API Endpoints</h3>

<ul>
    <li><code>/api/v1/chat</code>: Endpoint for interacting with the chatbot.</li>
    <li><code>/api/v1/speechtotext</code>: Endpoint for converting speech to text.</li>
    <li><code>/api/v1/texttospeech</code>: Endpoint for converting text to speech.</li>
</ul>

<h3>Examples</h3>

<h4>Example 1: Chatbot Interaction</h4>

<pre><code>import requests

url = "http://localhost:5000/api/v1/chat"
data = {"input": "What is the top speed of the latest Porsche 911?"}

response = requests.post(url, json=data)
print(response.json())
</code></pre>

<h4>Example 2: Speech-to-Text Conversion</h4>

<pre><code>import requests

url = "http://localhost:5000/api/v1/speechtotext"
audio_file = open("audio.wav", "rb")

files = {"audio": audio_file}

response = requests.post(url, files=files)
print(response.json())
</code></pre>

<h4>Example 3: Text-to-Speech Conversion</h4>

<pre><code>import requests

url = "http://localhost:5000/api/v1/texttospeech"
data = {"text": "The top speed of the latest Porsche 911 is 211 mph."}

response = requests.post(url, json=data)
audio_data = response.json()["audio"]

# Save audio data to a file or play it directly
</code></pre>

<h2>Contributing</h2>

<p>Contributions are welcome! Feel free to open issues for feature requests, bug fixes, or general improvements. Pull requests are also appreciated.</p>

<h2>License</h2>

<p>This project is licensed under the MIT License. See the <a href="LICENSE">LICENSE</a> file for details.</p>

</body>
</html>
