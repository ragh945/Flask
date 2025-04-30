

<h1>Flask Web Application</h1>

<p>This document provides an overview of Flask, Jinja templating, variable rules, and WSGI.</p>

<h2>What is Flask?</h2>
<p><strong>Flask</strong> is a lightweight and flexible web framework for Python. It is categorized as a <em>micro-framework</em> because it does not require particular tools or libraries, allowing developers to choose their components. Flask is simple to use and ideal for building web applications and APIs quickly.</p>

<h3>Why Use Flask?</h3>
<ul>
    <li>Minimalistic and easy to learn</li>
    <li>Great for small to medium web applications</li>
    <li>Extensible via numerous third-party libraries</li>
    <li>Built-in development server and debugger</li>
    <li>Integrated support for unit testing</li>
</ul>

<h2>What is Jinja2 Template Engine?</h2>
<p><strong>Jinja2</strong> is the template engine used by Flask. It allows you to embed Python-like expressions inside HTML files. This helps separate the business logic (Python code) from presentation (HTML templates).</p>

<h3>Common Jinja2 Syntax:</h3>
<ul>
    <li><code>{{ variable }}</code> – Output a variable's value</li>
    <li><code>{% if condition %}</code> … <code>{% endif %}</code> – Conditional statements</li>
    <li><code>{% for item in list %}</code> … <code>{% endfor %}</code> – Loops</li>
    <li><code>{# This is a comment #}</code> – Comments in templates</li>
</ul>

<h2>Flask Variable Rules (Dynamic Routes)</h2>
<p>Flask allows dynamic routing by including variables in the route URL:</p>

<pre><code>@app.route('/user/&lt;username&gt;')
def show_user_profile(username):
    return f"User: {username}"
</code></pre>

<p><strong>Types of Variable Rules:</strong></p>
<ul>
    <li><code>string</code>: (default) accepts any text without a slash</li>
    <li><code>int</code>: accepts only integers</li>
    <li><code>float</code>: accepts floating-point values</li>
    <li><code>path</code>: like string but allows slashes</li>
</ul>

<h2>What is WSGI?</h2>
<p><strong>WSGI (Web Server Gateway Interface)</strong> is a specification that defines how web servers communicate with web applications in Python. It acts as a bridge between your Flask app and the web server (like Gunicorn or uWSGI).</p>

<p>When you write a Flask app, you are essentially creating a WSGI application. Flask handles all the request/response logic internally while adhering to the WSGI standard.</p>

<pre><code>app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World!"
</code></pre>

<h2>Conclusion</h2>
<p>Flask is a powerful, minimal web framework in Python that allows rapid development with a clean separation of concerns using Jinja2. It supports WSGI and dynamic routing through variable rules, making it ideal for both APIs and full-stack web apps.</p>

</body>
</html>
