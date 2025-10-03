"""
Sample Flask application for testing the buildpack.
"""
from flask import Flask, jsonify
import os

app = Flask(__name__)


@app.route('/')
def index():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Flask App with pyproject.toml</title>
        <style>
            body {
                font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
                max-width: 800px;
                margin: 50px auto;
                padding: 20px;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
            }
            .container {
                background: rgba(255, 255, 255, 0.1);
                backdrop-filter: blur(10px);
                padding: 40px;
                border-radius: 20px;
                box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
            }
            h1 {
                margin-top: 0;
                font-size: 2.5em;
            }
            .status {
                background: rgba(255, 255, 255, 0.2);
                padding: 15px;
                border-radius: 10px;
                margin: 20px 0;
            }
            a {
                color: #fff;
                text-decoration: underline;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🚀 Flask App Running!</h1>
            <p>This Flask application was deployed using pyproject.toml for dependency management.</p>
            <div class="status">
                <h3>✅ Status: Healthy</h3>
                <p>Buildpack: Python Flask (pyproject.toml)</p>
            </div>
            <p>Try these endpoints:</p>
            <ul>
                <li><a href="/health">/health</a> - Health check</li>
                <li><a href="/api/info">/api/info</a> - App information</li>
            </ul>
        </div>
    </body>
    </html>
    '''


@app.route('/health')
def health():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'message': 'Application is running'
    })


@app.route('/api/info')
def info():
    """Return application information"""
    return jsonify({
        'app': 'Flask Sample App',
        'python_version': os.sys.version,
        'buildpack': 'python-flask-buildpack (pyproject.toml)',
        'environment': os.environ.get('FLASK_ENV', 'production')
    })


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)

