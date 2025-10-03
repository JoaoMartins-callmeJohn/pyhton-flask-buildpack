# Deploying the Buildpack

## Step 1: Push to GitHub

```bash
# Create a new repository on GitHub, then:
git remote add origin https://github.com/yourusername/pyhton-flask-buildpack.git
git branch -M main
git push -u origin main
```

## Step 2: Use in Dokku

Once pushed to GitHub, you can reference it in three ways:

### Method A: Set as the primary buildpack
```bash
dokku buildpacks:set <app-name> https://github.com/yourusername/pyhton-flask-buildpack.git
```

### Method B: Add to buildpack chain
```bash
dokku buildpacks:add <app-name> https://github.com/yourusername/pyhton-flask-buildpack.git
```

### Method C: Use a .buildpacks file in your app
Create a `.buildpacks` file in your Flask app repository:
```
https://github.com/yourusername/pyhton-flask-buildpack.git
```

## Step 3: Deploy Your Flask App

In your Flask application repository (the one with `pyproject.toml`):

```bash
# Add Dokku remote
git remote add dokku dokku@your-server.com:app-name

# Deploy
git push dokku main
```

## Using Specific Branches or Tags

You can reference specific versions:

```bash
# Use a specific branch
dokku buildpacks:set <app-name> https://github.com/yourusername/pyhton-flask-buildpack.git#development

# Use a specific tag
dokku buildpacks:set <app-name> https://github.com/yourusername/pyhton-flask-buildpack.git#v1.0.0

# Use a specific commit
dokku buildpacks:set <app-name> https://github.com/yourusername/pyhton-flask-buildpack.git#abc123
```

## Alternative: Using GitLab or Bitbucket

```bash
# GitLab
dokku buildpacks:set <app-name> https://gitlab.com/yourusername/pyhton-flask-buildpack.git

# Bitbucket
dokku buildpacks:set <app-name> https://bitbucket.org/yourusername/pyhton-flask-buildpack.git
```

## Alternative: Using a Private Repository

For private repositories, you may need to set up SSH keys or access tokens on your Dokku server.

### Using SSH (recommended for private repos):
```bash
dokku buildpacks:set <app-name> git@github.com:yourusername/pyhton-flask-buildpack.git
```

## Verifying the Buildpack

Check which buildpacks are set:
```bash
dokku buildpacks:list <app-name>
```

## Troubleshooting

### Virtual environment errors
The buildpack uses `virtualenv` instead of `venv` to avoid dependency on system packages like `python3-venv`. This makes it work reliably in containerized environments.

### Build logs
To see detailed build logs:
```bash
dokku ps:rebuild <app-name>
```

## Testing with the Example App

The `example/` directory contains a complete Flask app for testing:

```bash
# Copy example files to a new directory
cp -r example/ ../my-flask-test
cd ../my-flask-test

# Initialize git and deploy
git init
git add .
git commit -m "Initial commit"
git remote add dokku dokku@your-server.com:my-flask-test
git push dokku main
```

The buildpack will automatically detect the `pyproject.toml` file and build your app!

