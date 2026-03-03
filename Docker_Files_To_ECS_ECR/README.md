# Simple Python Docker example

Files added:

- `Dockerfile` — builds a small image running a Flask app on port 8080
- `app.py` — minimal Flask app
- `requirements.txt` — Flask dependency

Build and run locally (PowerShell):

```powershell
cd "C:\Users\KITS\OneDrive\Desktop\SDK_Mak1\Docker_Files"
docker build -t my-python-app:latest .
docker run --rm -p 8080:8080 my-python-app:latest
```

Then open http://localhost:8080 in your browser.

Optional: tag and push to ECR (replace with your repo URI):

```powershell
# Authenticate to ECR
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 700427002839.dkr.ecr.us-east-1.amazonaws.com

# Tag and push
docker tag my-python-app:latest 700427002839.dkr.ecr.us-east-1.amazonaws.com/ssdn-demo-app:latest
docker push 700427002839.dkr.ecr.us-east-1.amazonaws.com/ssdn-demo-app:latest
```
