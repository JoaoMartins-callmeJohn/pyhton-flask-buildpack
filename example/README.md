# Flask Sample Application

This is a sample Flask application to test the Python Flask buildpack with `pyproject.toml`.

## Local Development

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -e .
```

3. Run the application:
```bash
python app.py
```

Or with Gunicorn:
```bash
gunicorn app:app --bind 0.0.0.0:5000 --reload
```

4. Visit http://localhost:5000

## Deploy to Dokku

1. Create a Dokku app:
```bash
dokku apps:create flask-sample
```

2. Set the buildpack:
```bash
dokku buildpacks:set flask-sample https://github.com/yourusername/pyhton-flask-buildpack.git
```

3. Deploy:
```bash
git remote add dokku dokku@your-server:flask-sample
git push dokku main
```

## Endpoints

- `/` - Homepage
- `/health` - Health check (JSON)
- `/api/info` - Application information (JSON)

