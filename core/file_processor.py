import string
import secrets

class FileProcessor:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        
    def _generate_secret_key(self, length=50):
        """
        Generates a cryptographically secure Django SECRET_KEY.

        Args:
            length (int): Length of the generated key. Default is 50.

        Returns:
            str: A randomly generated secret key string.
        """
        chars = string.ascii_letters + string.digits + string.punctuation
        # Remove backslashes and quotes which can break the settings string
        chars = chars.replace("\\", "").replace('"', "").replace("'", "")
        return ''.join(secrets.choice(chars) for _ in range(length))
    
    def constants(self, template):
        """
        Holds all the constant file contents that should appear in all projects
        
        Args:
            template (str): The template type being used
            
        Returns:
            dict: Dictionary containing README and gitignore content
        """
        
        # Template-specific README content
        if template == "web-django":
            overview = self.description or "This project was bootstrapped with Inventrix, providing you a ready-to-code Django environment complete with a core app, default templates, and static assets."
            structure = f"""{self.name}/
├── core/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── templates/
│   └── index.html
├── static/
│   ├── css/
│   └── js/
├── manage.py
└── README.md
    """
            setup_steps = """
### 1. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate
```

### 2. Install dependencies
```bash
pip install django
```

### 3. Run migrations
```bash
python manage.py migrate
```

### 4. Start the development server
```bash
python manage.py runserver
```

Now open your browser and visit:
👉 http://127.0.0.1:8000/
    """

        elif template == "web-flask":
            overview = self.description or "This project was bootstrapped with Inventrix, providing you a ready-to-code Flask application with a clean structure."
            structure = f"""{self.name}/
├── app/
│   ├── __init__.py
│   ├── routes.py
│   └── models.py
├── templates/
│   └── index.html
├── static/
│   ├── css/
│   └── js/
├── run.py
└── README.md
    """
            setup_steps = """
### 1. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate
```

### 2. Install dependencies
```bash
pip install flask
```

### 3. Run the application
```bash
python run.py
```

Now open your browser and visit:
👉 http://127.0.0.1:5000/
    """

        elif template == "web-streamlit":
            overview = self.description or "This project was bootstrapped with Inventrix, providing you a ready-to-code Streamlit application for building interactive data apps."
            structure = f"""{self.name}/
├── app.py
├── pages/
├── utils/
├── requirements.txt
└── README.md
    """
            setup_steps = """
### 1. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate
```

### 2. Install dependencies
```bash
pip install streamlit
```

### 3. Run the application
```bash
streamlit run app.py
```

Your app will automatically open in your browser!
    """

        elif template == "ml-tensorflow":
            overview = self.description or "This project was bootstrapped with Inventrix, providing you a ready-to-code TensorFlow machine learning project structure."
            structure = f"""{self.name}/
├── data/
├── models/
├── notebooks/
├── src/
│   ├── train.py
│   └── evaluate.py
├── requirements.txt
└── README.md
    """
            setup_steps = """
### 1. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate
```

### 2. Install dependencies
```bash
pip install tensorflow numpy pandas matplotlib
```

### 3. Start training
```bash
python src/train.py
```
    """

        elif template == "ml-torch":
            overview = self.description or "This project was bootstrapped with Inventrix, providing you a ready-to-code PyTorch machine learning project structure."
            structure = f"""{self.name}/
├── data/
├── models/
├── notebooks/
├── src/
│   ├── train.py
│   └── evaluate.py
├── requirements.txt
└── README.md
    """
            setup_steps = """
### 1. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate
```

### 2. Install dependencies
```bash
pip install torch numpy pandas matplotlib
```

### 3. Start training
```bash
python src/train.py
```
    """

        elif template == "simulation":
            overview = self.description or "This project was bootstrapped with Inventrix, providing you a ready-to-code simulation framework."
            structure = f"""{self.name}/
├── src/
│   ├── main.py
│   └── simulation.py
├── config/
├── output/
├── requirements.txt
└── README.md
    """
            setup_steps = """### 1. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run simulation
```bash
python src/main.py
```
    """

        elif template == "automation":
            overview = self.description or "This project was bootstrapped with Inventrix, providing you a ready-to-code automation script framework."
            structure = f"""{self.name}/
├── scripts/
│   └── main.py
├── config/
├── logs/
├── requirements.txt
└── README.md
    """
            setup_steps = """### 1. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run automation
```bash
python scripts/main.py
```
    """

        else:  # vanilla
            overview = self.description or "This project was bootstrapped with Inventrix, providing you a clean Python project structure."
            structure = f"""{self.name}/
├── src/
│   └── main.py
├── tests/
├── requirements.txt
└── README.md
    """
            setup_steps = """### 1. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the project
```bash
python src/main.py
```
    """

        # Build the complete README
        README = f"""# {self.name.title()}

Welcome to **{self.name.title()}**, a project generated by **Inventrix CLI** – your intelligent project starter kit.

---

## 🚀 Overview

    {overview}

---

## 🧩 Project Structure

```
    {structure}
```

---

## ⚙️ Setup & Usage

    {setup_steps}

---

## 🪄 About Inventrix

Inventrix is a project manager and scaffolding tool that helps developers start smarter, faster, and more inspired.

> "Build once, invent forever." 💡

---

© {self.name.title()} – Generated with ❤️ by Inventrix CLI
    """
        
        # Base gitignore content
        gitignore_base = """# Python
__pycache__/
*.py[cod]
*$py.class
venv/
.env
"""
        
        # Template-specific gitignore additions
        if template == "web-django":
            template_specific = """# Database
db.sqlite3
*.db

# Django specific
/staticfiles/
/media/
/static/
/local_settings.py
"""
        elif template == "web-flask":
            template_specific = """# Database
*.db

# Flask specific
instance/
/static/
/templates/__pycache__/
"""
        elif template == "web-streamlit":
            template_specific = """# Streamlit
.streamlit/
.cache/
"""
        elif template in ("ml-torch", "ml-tensorflow"):
            template_specific = """# ML artifacts
data/
datasets/
runs/
checkpoints/
*.pt
*.pth
*.h5
.ipynb_checkpoints/
"""
        elif template == "simulation":
            template_specific = """# Simulation outputs
logs/
output/
reports/
temp/
"""
        elif template == "automation":
            template_specific = """# Automation logs
logs/
temp/
*.csv
*.json
"""
        else:
            template_specific = ""
        
        gitignore = gitignore_base + template_specific
        
        requirements = """
# Requirements for your project

        """
        if template == "web-django":
            template_specific = """
django
djangorestframework
django-cors-headers
django-filter
django-environ
django-allauth
djangorestframework-simplejwt
django-debug-toolbar
django-extensions
Pillow
django-storages
whitenoise
gunicorn
pytest-django
            """
            
        elif template == "web-flask":
            template_specific = """
# ----------------------------
# Core
# ----------------------------
Flask==3.0.3
Werkzeug==3.0.3
Jinja2==3.1.4
itsdangerous==2.2.0
click==8.1.7

# ----------------------------
# REST API + JSON
# ----------------------------
Flask-RESTful==0.3.10
Flask-Cors==4.0.1
Flask-RESTX==1.3.0
marshmallow==3.22.0
apispec==6.5.0

# ----------------------------
# Database & ORM
# ----------------------------
Flask-SQLAlchemy==3.1.1
SQLAlchemy==2.0.34
Flask-Migrate==4.1.0
alembic==1.14.0
psycopg2-binary==2.9.9    # PostgreSQL
pymysql==1.1.1            # MySQL
sqlite-utils==3.36.0

# ----------------------------
# Authentication & Security
# ----------------------------
Flask-Login==0.6.3
Flask-JWT-Extended==4.6.0
Flask-Bcrypt==1.0.1
Flask-Limiter==3.8.0

# ----------------------------
# Environment & Config
# ----------------------------
python-dotenv==1.0.1
dynaconf==3.2.6

# ----------------------------
# Background Jobs & Caching
# ----------------------------
Flask-Caching==2.3.0
Celery==5.4.0
redis==5.1.0

# ----------------------------
# Testing & Dev Tools
# ----------------------------
pytest==8.3.3
pytest-flask==1.3.0
coverage==7.6.4
black==24.10.0
flake8==7.1.1
isort==5.13.2

# ----------------------------
# Deployment
# ----------------------------
gunicorn==23.0.0
gevent==24.10.1
whitenoise==6.7.0

            """
            
        elif template == "web-streamlit":
            template_specific = """
# ----------------------------
# Core
# ----------------------------
streamlit==1.39.0
altair==5.4.1
pydeck==0.9.1
protobuf==5.28.2
watchdog==5.0.3

# ----------------------------
# Data Handling
# ----------------------------
pandas==2.2.3
numpy==2.1.2
pyarrow==17.0.0
openpyxl==3.1.5
requests==2.32.3

# ----------------------------
# Visualization & Dashboarding
# ----------------------------
plotly==5.24.1
matplotlib==3.9.2
seaborn==0.13.2
streamlit-option-menu==0.3.13
streamlit-extras==0.5.0
streamlit-lottie==0.0.5

# ----------------------------
# Caching, Environment, & Utils
# ----------------------------
python-dotenv==1.0.1
pytz==2024.2
Pillow==10.4.0

# ----------------------------
# Deployment
# ----------------------------
gunicorn==23.0.0

            """
        
        elif template == "ml-torch":
            template_specific = """
# Core PyTorch
torch
torchvision
torchaudio

# For tabular / data preprocessing
pandas
numpy
scikit-learn

# For model visualization / progress tracking
matplotlib
seaborn
tqdm

# For deep learning utilities
torchmetrics
pytorch-lightning      # optional, for structured training loops
torchsummary           # optional, for model summaries
torchinfo              # optional, modern replacement for torchsummary

# For experiment tracking (optional but common)
tensorboard
wandb                  # Weights & Biases
mlflow

# For optimization and scheduling (optional)
optuna                 # hyperparameter tuning
transformers           # if using pretrained models
accelerate             # for distributed or mixed-precision training

            """
            
        elif template == "ml-tensorflow":
            template_specific = """
# Core TensorFlow
tensorflow
tensorflow-hub
tensorflow-datasets
tensorflow-addons
tensorflow-io

# For data handling
numpy
pandas
scikit-learn

# For visualization and monitoring
matplotlib
seaborn
tensorboard

# For optimization and experiment tracking (optional)
optuna
mlflow
wandb

# For model deployment / serving (optional)
tensorflow-serving-api
tensorflow-model-optimization
tensorflowjs               # for web deployment
tflite-support              # for mobile / edge deployment

            """
            
        elif template == "simulation":
            template_specific = """
# Core scientific computing
numpy
scipy
pandas
matplotlib

# Visualization & animation
seaborn
plotly
matplotlib-animation
ipywidgets

# Random processes & statistics
sympy
statsmodels

# Optimization and numerical solvers
numba
scikit-optimize

# Parallelism / speed
multiprocessing
joblib
tqdm

# Optional: simulation-specific frameworks
simpy                # Discrete-event simulation
mesa                 # Agent-based modeling
pybullet             # Physics simulation
gymnasium            # RL simulation environments
pygame               # 2D simulation/visualization (simple)

# Optional: if doing ML-based simulation
torch                # or tensorflow, depending on project
stable-baselines3    # for reinforcement learning simulations
            """
            
        elif template == "automation":
            template_specific = """
# Core utilities
os
sys
subprocess
shutil
pathlib
logging

# Task scheduling / time
schedule
apscheduler
datetime
time

# File and data handling
pandas
openpyxl
csv
json
yaml

# CLI and environment
argparse
click
python-dotenv

# Web / HTTP automation
requests
beautifulsoup4
selenium
playwright
httpx

# Browser automation (modern)
undetected-chromedriver
pyppeteer

# System / desktop automation
pyautogui
keyboard
mouse
psutil

# Parallel / async tasks
asyncio
concurrent.futures
multiprocessing
threading
tqdm

# APIs and automation frameworks
fastapi
flask
airflow          # workflow automation
prefect          # modern orchestration
celery           # distributed task automation

            """
            
        else:
            template_specific = ""
            
        requirements = requirements + template_specific
        
        return {
            "README": README,
            "gitignore": gitignore,
            "requirements": requirements
        }

    
    def django(self):
        """
        Contains all the files for the django template
        
        Args:
            None
        
        Return:
            Complete file content for core files in django projects.
        """
      
        SECRET_KEY = self._generate_secret_key()
                
        content = {
        "manage" : f"""# Manage file content
import os
import sys


def main():
    # Run administrative tasks
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "{self.name}.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
    
            """,
            
            "asgi" : f"""
import os

from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "{self.name}.settings")

application = get_asgi_application()

            """,
            
            "settings" : f"""
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = "{SECRET_KEY}"

DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "core"
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "{self.name}.urls"

TEMPLATES = [
    {{
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR/"templates"],
        "APP_DIRS": True,
        "OPTIONS": {{
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        }},
    }},
]

WSGI_APPLICATION = "{self.name}.wsgi.application"


# Database

DATABASES = {{
    "default": {{
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }}
}}


# Password validation

AUTH_PASSWORD_VALIDATORS = [
    {{
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    }},
    {{
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    }},
    {{
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    }},
    {{
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    }},
]


# Internationalization

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)

STATIC_URL = "static/"

# Default primary key field type

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

            """,
            
            "urls_main" : """
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("core.urls"))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

            """,
           
            "wsgi" : f"""
import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "{self.name}.settings")

application = get_wsgi_application()

            """,
            
            "admin" : """
from django.contrib import admin

# Register your models here.

            """,
            
            "models" : """
from django.db import models

# Create your models here.

            """,
            
            "apps" : """
from django.apps import AppConfig


class CoreConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "core"

            """,
            
            "tests" : """
from django.test import TestCase

# Create your tests here.

            """,
            
            "urls_app" : """
from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path("", views.index, name="index"),
]

            """,
            
            "views" : """
from django.shortcuts import render

# Create your views here.
def index(requests):
    return render(requests, 'index.html')

            """,
            
            "index" : """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>It worked! - Inventrix</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Inter', sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 20px;
        }

        .container {
            background: white;
            border-radius: 20px;
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
            max-width: 800px;
            width: 100%;
            overflow: hidden;
            animation: slideUp 0.6s ease-out;
        }

        @keyframes slideUp {
            from {
                opacity: 0;
                transform: translateY(30px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        .header {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 50px 40px;
            text-align: center;
            color: white;
        }

        .success-icon {
            width: 80px;
            height: 80px;
            margin: 0 auto 20px;
            background: rgba(255, 255, 255, 0.2);
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            animation: bounce 1s ease infinite;
        }

        @keyframes bounce {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-10px); }
        }

        .success-icon svg {
            width: 50px;
            height: 50px;
        }

        h1 {
            font-size: 48px;
            font-weight: 700;
            margin-bottom: 10px;
            text-shadow: 0 2px 10px rgba(0, 0, 0, 0.2);
        }

        .subtitle {
            font-size: 20px;
            opacity: 0.95;
        }

        .content {
            padding: 40px;
        }

        .success-message {
            background: #e8f5e9;
            border-left: 4px solid #4caf50;
            padding: 20px;
            border-radius: 8px;
            margin-bottom: 30px;
        }

        .success-message h2 {
            color: #2e7d32;
            font-size: 24px;
            margin-bottom: 10px;
        }

        .success-message p {
            color: #1b5e20;
            line-height: 1.6;
        }

        .info-box {
            background: #f5f5f5;
            padding: 25px;
            border-radius: 12px;
            margin-bottom: 25px;
        }

        .info-box h3 {
            color: #333;
            font-size: 18px;
            margin-bottom: 15px;
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .info-box ul {
            list-style: none;
            padding-left: 0;
        }

        .info-box li {
            color: #666;
            line-height: 2;
            padding-left: 25px;
            position: relative;
        }

        .info-box li:before {
            content: "✓";
            position: absolute;
            left: 0;
            color: #667eea;
            font-weight: bold;
        }

        .next-steps {
            background: linear-gradient(135deg, #fff5e6 0%, #ffe6f0 100%);
            padding: 25px;
            border-radius: 12px;
            margin-bottom: 25px;
        }

        .next-steps h3 {
            color: #d84315;
            font-size: 18px;
            margin-bottom: 15px;
        }

        .next-steps p {
            color: #555;
            line-height: 1.8;
            margin-bottom: 15px;
        }

        .code-snippet {
            background: #2d2d2d;
            color: #f8f8f2;
            padding: 15px;
            border-radius: 8px;
            font-family: 'Courier New', monospace;
            font-size: 14px;
            margin: 10px 0;
            overflow-x: auto;
        }

        .fun-fact {
            background: linear-gradient(135deg, #fff9c4 0%, #fff59d 100%);
            padding: 20px;
            border-radius: 12px;
            border: 2px dashed #fbc02d;
            text-align: center;
        }

        .fun-fact p {
            color: #f57f17;
            font-size: 16px;
            font-weight: 600;
            margin: 0;
        }

        .emoji {
            font-size: 24px;
            margin-right: 8px;
        }

        .footer {
            background: #f9f9f9;
            padding: 20px 40px;
            text-align: center;
            color: #666;
            border-top: 1px solid #e0e0e0;
        }

        .footer p {
            margin: 5px 0;
        }

        .heart {
            color: #e91e63;
            animation: heartbeat 1.5s ease infinite;
        }

        @keyframes heartbeat {
            0%, 100% { transform: scale(1); }
            10%, 30% { transform: scale(1.1); }
            20%, 40% { transform: scale(1); }
        }

        a {
            color: #667eea;
            text-decoration: none;
            font-weight: 600;
        }

        a:hover {
            text-decoration: underline;
        }

        @media (max-width: 600px) {
            h1 {
                font-size: 36px;
            }
            
            .header {
                padding: 40px 20px;
            }
            
            .content {
                padding: 30px 20px;
            }
            
            .footer {
                padding: 20px;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <div class="success-icon">
                <svg viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="3">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7" />
                </svg>
            </div>
            <h1>It worked!</h1>
            <p class="subtitle">Your Inventrix project is up and running 🎉</p>
        </div>

        <div class="content">
            <div class="success-message">
                <h2>🎊 Congratulations!</h2>
                <p>You've successfully created and launched your project with <strong>Inventrix</strong>. Everything is set up and ready for you to start building something amazing!</p>
            </div>

            <div class="info-box">
                <h3><span class="emoji">📦</span>What's already set up for you:</h3>
                <ul>
                    <li>Complete project structure following best practices</li>
                    <li>Pre-configured settings and dependencies</li>
                    <li>Database ready to use (just run migrations!)</li>
                    <li>Static files structure for CSS and JavaScript</li>
                    <li>Sample templates to get you started</li>
                </ul>
            </div>

            <div class="next-steps">
                <h3><span class="emoji">🚀</span>Ready to start coding?</h3>
                <p>Here are some things you can do next:</p>
                <ul style="list-style: none; padding: 0;">
                    <li style="margin-bottom: 10px;"><strong>1.</strong> Edit <code style="background: rgba(0,0,0,0.1); padding: 2px 6px; border-radius: 4px;">core/views.py</code> to add your own views</li>
                    <li style="margin-bottom: 10px;"><strong>2.</strong> Create models in <code style="background: rgba(0,0,0,0.1); padding: 2px 6px; border-radius: 4px;">core/models.py</code></li>
                    <li style="margin-bottom: 10px;"><strong>3.</strong> Customize <code style="background: rgba(0,0,0,0.1); padding: 2px 6px; border-radius: 4px;">templates/index.html</code> with your content</li>
                    <li><strong>4.</strong> Check out the README.md for detailed instructions</li>
                </ul>
            </div>

            <div class="fun-fact">
                <p><span class="emoji">💡</span> Pro tip: All the boilerplate is done! Focus on building features, not infrastructure.</p>
            </div>
        </div>

        <div class="footer">
            <p>Generated with <span class="heart">❤️</span> by <strong>Inventrix CLI</strong></p>
            <p style="font-size: 14px; margin-top: 10px;">Build once, invent forever 💫</p>
        </div>
    </div>
</body>
</html>
            """
        }
        
        return content
    
    def flask(self):
        """
        Holds all content for flask templated projects
        """
        
        flask_content = {
        
        "app": """
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)

        """,
        
        "config": """
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key'
    DEBUG = os.environ.get('FLASK_DEBUG', 'True').lower() == 'true'
        """,
        
        "env": """
SECRET_KEY=your-secret-key-here
FLASK_DEBUG=True
        """,
        
        "index": """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>It worked! - Inventrix</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Inter', sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 20px;
        }

        .container {
            background: white;
            border-radius: 20px;
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
            max-width: 800px;
            width: 100%;
            overflow: hidden;
            animation: slideUp 0.6s ease-out;
        }

        @keyframes slideUp {
            from {
                opacity: 0;
                transform: translateY(30px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        .header {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 50px 40px;
            text-align: center;
            color: white;
        }

        .success-icon {
            width: 80px;
            height: 80px;
            margin: 0 auto 20px;
            background: rgba(255, 255, 255, 0.2);
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            animation: bounce 1s ease infinite;
        }

        @keyframes bounce {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-10px); }
        }

        .success-icon svg {
            width: 50px;
            height: 50px;
        }

        h1 {
            font-size: 48px;
            font-weight: 700;
            margin-bottom: 10px;
            text-shadow: 0 2px 10px rgba(0, 0, 0, 0.2);
        }

        .subtitle {
            font-size: 20px;
            opacity: 0.95;
        }

        .content {
            padding: 40px;
        }

        .success-message {
            background: #e8f5e9;
            border-left: 4px solid #4caf50;
            padding: 20px;
            border-radius: 8px;
            margin-bottom: 30px;
        }

        .success-message h2 {
            color: #2e7d32;
            font-size: 24px;
            margin-bottom: 10px;
        }

        .success-message p {
            color: #1b5e20;
            line-height: 1.6;
        }

        .info-box {
            background: #f5f5f5;
            padding: 25px;
            border-radius: 12px;
            margin-bottom: 25px;
        }

        .info-box h3 {
            color: #333;
            font-size: 18px;
            margin-bottom: 15px;
            display: flex;
            align-items: center;
            gap: 10px;
        }

        .info-box ul {
            list-style: none;
            padding-left: 0;
        }

        .info-box li {
            color: #666;
            line-height: 2;
            padding-left: 25px;
            position: relative;
        }

        .info-box li:before {
            content: "✓";
            position: absolute;
            left: 0;
            color: #667eea;
            font-weight: bold;
        }

        .next-steps {
            background: linear-gradient(135deg, #fff5e6 0%, #ffe6f0 100%);
            padding: 25px;
            border-radius: 12px;
            margin-bottom: 25px;
        }

        .next-steps h3 {
            color: #d84315;
            font-size: 18px;
            margin-bottom: 15px;
        }

        .next-steps p {
            color: #555;
            line-height: 1.8;
            margin-bottom: 15px;
        }

        .code-snippet {
            background: #2d2d2d;
            color: #f8f8f2;
            padding: 15px;
            border-radius: 8px;
            font-family: 'Courier New', monospace;
            font-size: 14px;
            margin: 10px 0;
            overflow-x: auto;
        }

        .fun-fact {
            background: linear-gradient(135deg, #fff9c4 0%, #fff59d 100%);
            padding: 20px;
            border-radius: 12px;
            border: 2px dashed #fbc02d;
            text-align: center;
        }

        .fun-fact p {
            color: #f57f17;
            font-size: 16px;
            font-weight: 600;
            margin: 0;
        }

        .emoji {
            font-size: 24px;
            margin-right: 8px;
        }

        .footer {
            background: #f9f9f9;
            padding: 20px 40px;
            text-align: center;
            color: #666;
            border-top: 1px solid #e0e0e0;
        }

        .footer p {
            margin: 5px 0;
        }

        .heart {
            color: #e91e63;
            animation: heartbeat 1.5s ease infinite;
        }

        @keyframes heartbeat {
            0%, 100% { transform: scale(1); }
            10%, 30% { transform: scale(1.1); }
            20%, 40% { transform: scale(1); }
        }

        a {
            color: #667eea;
            text-decoration: none;
            font-weight: 600;
        }

        a:hover {
            text-decoration: underline;
        }

        @media (max-width: 600px) {
            h1 {
                font-size: 36px;
            }
            
            .header {
                padding: 40px 20px;
            }
            
            .content {
                padding: 30px 20px;
            }
            
            .footer {
                padding: 20px;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <div class="success-icon">
                <svg viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="3">
                    <path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7" />
                </svg>
            </div>
            <h1>It worked!</h1>
            <p class="subtitle">Your Inventrix project is up and running 🎉</p>
        </div>

        <div class="content">
            <div class="success-message">
                <h2>🎊 Congratulations!</h2>
                <p>You've successfully created and launched your project with <strong>Inventrix</strong>. Everything is set up and ready for you to start building something amazing!</p>
            </div>

            <div class="info-box">
                <h3><span class="emoji">📦</span>What's already set up for you:</h3>
                <ul>
                    <li>Complete project structure following best practices</li>
                    <li>Pre-configured settings and dependencies</li>
                    <li>Database ready to use (just run migrations!)</li>
                    <li>Static files structure for CSS and JavaScript</li>
                    <li>Sample templates to get you started</li>
                </ul>
            </div>

            <div class="next-steps">
                <h3><span class="emoji">🚀</span>Ready to start coding?</h3>
                <p>Here are some things you can do next:</p>
                <ul style="list-style: none; padding: 0;">
                    <li style="margin-bottom: 10px;"><strong>1.</strong> Edit <code style="background: rgba(0,0,0,0.1); padding: 2px 6px; border-radius: 4px;">core/views.py</code> to add your own views</li>
                    <li style="margin-bottom: 10px;"><strong>2.</strong> Create models in <code style="background: rgba(0,0,0,0.1); padding: 2px 6px; border-radius: 4px;">core/models.py</code></li>
                    <li style="margin-bottom: 10px;"><strong>3.</strong> Customize <code style="background: rgba(0,0,0,0.1); padding: 2px 6px; border-radius: 4px;">templates/index.html</code> with your content</li>
                    <li><strong>4.</strong> Check out the README.md for detailed instructions</li>
                </ul>
            </div>

            <div class="fun-fact">
                <p><span class="emoji">💡</span> Pro tip: All the boilerplate is done! Focus on building features, not infrastructure.</p>
            </div>
        </div>

        <div class="footer">
            <p>Generated with <span class="heart">❤️</span> by <strong>Inventrix CLI</strong></p>
            <p style="font-size: 14px; margin-top: 10px;">Build once, invent forever 💫</p>
        </div>
    </div>
</body>
</html>
        """
        
        }
        
        return flask_content
    
    def streamlit(self):
        """
        streamlit file contents
        
        Args:
            None
            
        Returns a dict of the file contents
        """
        
        content = {
            "app": """
import streamlit as st
from landing import show_landing_page

def main():
    # Set page configuration
    st.set_page_config(
        page_title="Inventrix - Welcome",
        page_icon="✅",
        layout="centered",
        initial_sidebar_state="collapsed"
    )
    
    # Show the landing page
    show_landing_page()

if __name__ == "__main__":
    main()
            """,
            
            "landing": """
import streamlit as st

def show_landing_page():
    # Custom CSS to mimic the original design
    st.markdown(\"\"\"
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');
        
        body {
            font-family: 'Inter', sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            margin: 0;
            padding: 0;
        }
        
        .main-header {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 50px 40px;
            text-align: center;
            color: white;
            border-radius: 20px 20px 0 0;
            position: relative;
            overflow: hidden;
        }
        
        .success-icon {
            width: 80px;
            height: 80px;
            margin: 0 auto 20px;
            background: rgba(255, 255, 255, 0.2);
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            animation: bounce 1s ease infinite;
        }
        
        @keyframes bounce {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-10px); }
        }
        
        .success-message {
            background: #e8f5e9;
            border-left: 4px solid #4caf50;
            padding: 20px;
            border-radius: 8px;
            margin-bottom: 30px;
        }
        
        .info-box {
            background: #f5f5f5;
            padding: 25px;
            border-radius: 12px;
            margin-bottom: 25px;
        }
        
        .next-steps {
            background: linear-gradient(135deg, #fff5e6 0%, #ffe6f0 100%);
            padding: 25px;
            border-radius: 12px;
            margin-bottom: 25px;
        }
        
        .fun-fact {
            background: linear-gradient(135deg, #fff9c4 0%, #fff59d 100%);
            padding: 20px;
            border-radius: 12px;
            border: 2px dashed #fbc02d;
            text-align: center;
        }
        
        .footer {
            background: #f9f9f9;
            padding: 20px;
            text-align: center;
            color: #666;
            border-top: 1px solid #e0e0e0;
            border-radius: 0 0 20px 20px;
        }
        
        .heart {
            color: #e91e63;
            animation: heartbeat 1.5s ease infinite;
        }
        
        @keyframes heartbeat {
            0%, 100% { transform: scale(1); }
            10%, 30% { transform: scale(1.1); }
            20%, 40% { transform: scale(1); }
        }
        
        .container {
            max-width: 800px;
            margin: 0 auto;
            background: white;
            border-radius: 20px;
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
            overflow: hidden;
            animation: slideUp 0.6s ease-out;
        }
        
        @keyframes slideUp {
            from {
                opacity: 0;
                transform: translateY(30px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }
        
        .emoji {
            font-size: 24px;
            margin-right: 8px;
        }
        
        .code-snippet {
            background: #2d2d2d;
            color: #f8f8f2;
            padding: 15px;
            border-radius: 8px;
            font-family: 'Courier New', monospace;
            font-size: 14px;
            margin: 10px 0;
            overflow-x: auto;
        }
    </style>
    \"\"\", unsafe_allow_html=True)
    
    # Container div
    st.markdown('<div class="container">', unsafe_allow_html=True)
    
    # Header section
    st.markdown(\"\"\"
    <div class="main-header">
        <div class="success-icon">
            <svg viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="3" width="50" height="50">
                <path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7" />
            </svg>
        </div>
        <h1 style="font-size: 48px; font-weight: 700; margin-bottom: 10px; text-shadow: 0 2px 10px rgba(0, 0, 0, 0.2);">It worked!</h1>
        <p style="font-size: 20px; opacity: 0.95;">Your Inventrix project is up and running 🎉</p>
    </div>
    \"\"\", unsafe_allow_html=True)
    
    # Content section
    st.markdown(\"\"\"
    <div style="padding: 40px;">
        <div class="success-message">
            <h2 style="color: #2e7d32; font-size: 24px; margin-bottom: 10px;">🎊 Congratulations!</h2>
            <p style="color: #1b5e20; line-height: 1.6;">You've successfully created and launched your project with <strong>Inventrix</strong>. Everything is set up and ready for you to start building something amazing!</p>
        </div>

        <div class="info-box">
            <h3 style="color: #333; font-size: 18px; margin-bottom: 15px; display: flex; align-items: center; gap: 10px;">
                <span class="emoji">📦</span>What's already set up for you:
            </h3>
            <ul style="list-style: none; padding-left: 0;">
                <li style="color: #666; line-height: 2; padding-left: 25px; position: relative;">✓ Complete project structure following best practices</li>
                <li style="color: #666; line-height: 2; padding-left: 25px; position: relative;">✓ Pre-configured settings and dependencies</li>
                <li style="color: #666; line-height: 2; padding-left: 25px; position: relative;">✓ Database ready to use (just run migrations!)</li>
                <li style="color: #666; line-height: 2; padding-left: 25px; position: relative;">✓ Static files structure for CSS and JavaScript</li>
                <li style="color: #666; line-height: 2; padding-left: 25px; position: relative;">✓ Sample templates to get you started</li>
            </ul>
        </div>

        <div class="next-steps">
            <h3 style="color: #d84315; font-size: 18px; margin-bottom: 15px;">
                <span class="emoji">🚀</span>Ready to start coding?
            </h3>
            <p style="color: #555; line-height: 1.8; margin-bottom: 15px;">Here are some things you can do next:</p>
            <ol style="padding-left: 20px; color: #555; line-height: 1.8;">
                <li>Edit <code style="background: rgba(0,0,0,0.1); padding: 2px 6px; border-radius: 4px;">core/views.py</code> to add your own views</li>
                <li>Create models in <code style="background: rgba(0,0,0,0.1); padding: 2px 6px; border-radius: 4px;">core/models.py</code></li>
                <li>Customize <code style="background: rgba(0,0,0,0.1); padding: 2px 6px; border-radius: 4px;">templates/index.html</code> with your content</li>
                <li>Check out the README.md for detailed instructions</li>
            </ol>
        </div>

        <div class="fun-fact">
            <p style="color: #f57f17; font-size: 16px; font-weight: 600; margin: 0;">
                <span class="emoji">💡</span> Pro tip: All the boilerplate is done! Focus on building features, not infrastructure.
            </p>
        </div>
    </div>
    \"\"\", unsafe_allow_html=True)
    
    # Footer section
    st.markdown(\"\"\"
    <div class="footer">
        <p>Generated with <span class="heart">❤️</span> by <strong>Inventrix CLI</strong></p>
        <p style="font-size: 14px; margin-top: 10px;">Build once, invent forever 💫</p>
    </div>
    </div>
    \"\"\", unsafe_allow_html=True)
            """
        }
        
        return content