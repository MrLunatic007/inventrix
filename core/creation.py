import os
import shutil
import subprocess
import platform
from pathlib import Path

from core import file_processor

class Creator:
    """
    Responsible for creating the folder and adding files to the folders

    Args:
        name (str): The project name
        description (str): The project description
        template (str): The template type for the project

    Returns:
        A complete file structure with all the files intact and with sample code
    """

    VALID_TEMPLATES = [
        "web-django",
        "web-flask", 
        "web-streamlit",
        "ml-tensorflow",
        "ml-torch",
        "simulation",
        "automation",
        "vanilla"
    ]

    def __init__(self, name: str, description: str, template: str):
        self.name = name
        self.description = description
        self.template = template
        self.processor = file_processor.FileProcessor(name, description)
        self.base_path = Path(name).resolve()  # Use absolute path
        self.original_dir = Path.cwd()  # Store original directory

    def _write_file(self, filepath: str, content: str = ""):
        """Helper method to safely write files"""
        try:
            # Use relative path from current directory instead of base_path
            path = Path(filepath)
            path.parent.mkdir(parents=True, exist_ok=True)
            with open(path, 'w', encoding='utf-8') as f:
                f.write(content)
        except Exception as e:
            print(f"Error writing {filepath}: {e}")
            raise

    def creating_project_structure(self):
        """
        Creates the file structure according to the template selected

        Args:
            None

        Returns:
            A complete file structure as per the template
        """
        
        # Checking if the folder exists and removing it to avoid conflict
        if self.base_path.exists():
            print(f"Note: Removing existing {self.name}.")
            shutil.rmtree(self.base_path)
            
        # Create the project directory
        self.base_path.mkdir(parents=True)
        
        # Change to the project directory
        os.chdir(self.base_path)
        
        # Create common directories (now we're inside the project directory)
        Path("tests").mkdir(exist_ok=True)
        Path("docs").mkdir(exist_ok=True)
        
        
        # Get constants and write common files
        constants = self.processor.constants(self.template)
        
        self._write_file("requirements.txt", constants["requirements"])
        self._write_file("README.md", constants["README"])  # Fixed: was writing requirements
        self._write_file(".gitignore", constants["gitignore"])  # Added: missing gitignore
        
        self.python_venv()
        
        try:
            template_methods = {
                "web-django": self.django_structure,
                "web-flask": self.flask_structure,  # Fixed typo
                "web-streamlit": self.streamlit_structure,
                "ml-tensorflow": self.ml_tensorflow_structure,
                "ml-torch": self.ml_torch_structure,
                "simulation": self.simulation_structure,
                "automation": self.automation_structure,
                "vanilla": self.vanilla_structure
            }
            
            method = template_methods.get(self.template)
            if method:
                method()
            else:
                raise ValueError(f"Unknown template: {self.template}")
                
        except Exception as e:
            print(f"Error during structure creation: {e}")
            raise
        finally:
            # Return to original directory
            os.chdir(self.original_dir)
            
    def python_venv(self, requirements: str = "requirements.txt"):
        """
        Making a python virtual environment and installs the requirements
        
        Args: 
            requirements (str): Requirements file path
        """
        
        print("Making virtual environment: 'venv'")
        subprocess.run("python -m venv venv", shell=True, check=True)  # Fixed: added shell=True
        
        # Fixed: platform.system is a method
        if platform.system() == "Windows":
            activate_cmd = "venv\\Scripts\\activate.bat"
        else:
            activate_cmd = "source venv/bin/activate"
            
        try:
            print("Installing requirements...")
            # Fixed: proper command chaining
            if platform.system() == "Windows":
                cmd = "venv\\Scripts\\pip.exe install -r requirements.txt"
            else:
                cmd = "venv/bin/pip install -r requirements.txt"
            
            subprocess.run(cmd, shell=True, check=True)
            print("Requirements successfully installed.")
        except subprocess.CalledProcessError as e:
            print(f"Error occurred when setting up virtual environment: {e}")
            raise
            
    def django_structure(self):
        """
        All django file structure creation
        
        Args:
            None
            
        Returns:
            Complete django file structure
        """

        # Create directories
        Path(self.name).mkdir()
        Path("core").mkdir()
        Path("core/migrations").mkdir()  # Added: missing migrations
        Path("templates").mkdir()  # Fixed: should be at root level
        Path("static").mkdir()
        Path("static/css").mkdir()
        Path("static/js").mkdir()
        
        content = self.processor.django()
        
        # Write Django files
        self._write_file("manage.py", content["manage"])
        self._write_file(f"{self.name}/__init__.py", "")
        self._write_file(f"{self.name}/asgi.py", content["asgi"])
        self._write_file(f"{self.name}/settings.py", content["settings"])
        self._write_file(f"{self.name}/urls.py", content["urls_main"])
        self._write_file(f"{self.name}/wsgi.py", content["wsgi"])
        
        # Write core app files
        self._write_file("core/__init__.py", "")
        self._write_file("core/migrations/__init__.py", "")  # Added
        self._write_file("core/admin.py", content["admin"])
        self._write_file("core/apps.py", content["apps"])
        self._write_file("core/models.py", content["models"])
        self._write_file("core/tests.py", content["tests"])
        self._write_file("core/urls.py", content["urls_app"])
        self._write_file("core/views.py", content["views"])
        
        self._write_file("templates/index.html", content["index"])

    def flask_structure(self):  # Fixed: typo in method name
        """
        All Flask file structure creation 
        
        Args: 
            None
            
        Returns:
            Complete flask structure
        """
        
        # Create directories
        Path("templates").mkdir()
        Path("static").mkdir()
        Path("static/css").mkdir()
        Path("static/js").mkdir()
        
        flask_content = self.processor.flask()
        
        self._write_file("__init__.py", "")
        self._write_file("templates/index.html", flask_content["index"])
        self._write_file("static/css/style.css", "")
        self._write_file("static/js/script.js", "")  # Added .js extension
        self._write_file("app.py", flask_content["app"])
        self._write_file(".env", flask_content["env"])
                     
    def streamlit_structure(self):
        """All streamlit file structure creation 
        
        Args: 
            None
            
        Returns:
            Complete streamlit structure"""
            
        streamlit_content = self.processor.streamlit()
        
        Path("pages").mkdir()
        
        self._write_file("app.py", streamlit_content["app"])
        self._write_file("pages/landing.py", streamlit_content["landing"])
            
    def ml_tensorflow_structure(self):
        """All Machine learning tensorflow file structure creation 
        
        Args: 
            None
            
        Returns:
            Complete tensorflow file structure
        """
        # Create directories
        directories = [
            "data/raw",
            "data/processed", 
            "data/external",
            "notebooks",
            "src/data",
            "src/config",
            "src/models",
            "src/training",
            "src/evaluation",
            "src/utils"
        ]
        
        for directory in directories:
            Path(directory).mkdir(parents=True, exist_ok=True)
        
        # Write files
        self._write_file("src/data/__init__.py", "")
        self._write_file("src/data/dataset.py", "# Write your data processing pipeline here\n")
        self._write_file("src/config/config.yaml", "# Write your model configuration here\n")
        self._write_file("src/models/model.py", "# Write your model architecture here\nimport tensorflow as tf\n")
        self._write_file("src/evaluation/metrics.py", "# Write your metrics evaluation here\n")
        self._write_file("src/evaluation/visualization.py", 
                        "# Write your visualization evaluation here\nimport matplotlib.pyplot as plt\nimport seaborn as sns\n")
        self._write_file("src/training/trainer.py", "# Write your training logic here")
        self._write_file("src/utils/logger.py", "# Write your logging here\nimport logging\n")
        self._write_file("main.py", "# Put it all together here")
    
    def ml_torch_structure(self):
        """All Machine learning torch file structure creation 
        
        Args: 
            None
            
        Returns:
            Complete torch file structure"""
            
        # Create directories
        directories = [
            "data/raw",
            "data/processed",
            "data/external",
            "notebooks",
            "src/data",
            "src/config",
            "src/models",
            "src/training",
            "src/evaluation",
            "src/utils"
        ]
        
        for directory in directories:
            Path(directory).mkdir(parents=True, exist_ok=True)
        
        # Write files
        self._write_file("src/data/__init__.py", "")
        self._write_file("src/data/dataset.py", "# Write your data processing pipeline here\n")
        self._write_file("src/config/config.yaml", "# Write your model configuration here\n")
        self._write_file("src/models/model.py", "# Write your model architecture here\nimport torch\n")
        self._write_file("src/evaluation/metrics.py", "# Write your metrics evaluation here\n")
        # Fixed: double import and typo in filename
        self._write_file("src/evaluation/visualization.py",
                        "# Write your visualization evaluation here\nimport matplotlib.pyplot as plt\nimport seaborn as sns\n")
        self._write_file("src/utils/logger.py", "# Write your logging here\nimport logging\n")
        self._write_file("main.py", "# Put it all together here")
            
    def simulation_structure(self):
        """All simulation file structure creation 
        
        Args: 
            None
            
        Returns:
            Complete simulation file structure"""
            
        # Create directories
        directories = [
            "data/input",
            "data/logs",
            "data/results",
            "src/core",
            "src/configs",
            "src/visualization",
            "src/analysis"
        ]
        
        for directory in directories:
            Path(directory).mkdir(parents=True, exist_ok=True)
        
        self._write_file("src/core/__init__.py", "")
        self._write_file("src/core/environment.py", "# Write your environments here\n")
        self._write_file("src/core/entities.py", "# Write your entities here\n")
        self._write_file("src/core/physics.py", "# Give physics to your simulation\n")
        self._write_file("main.py", "# Put it all together now\n")
        self._write_file("config.yaml", "# Write your simulation configs\n")
    
    def automation_structure(self):
        """All automation file structure creation 
        
        Args: 
            None
            
        Returns:
            Complete automation file structure"""
            
        # Create directories
        Path("src/core").mkdir(parents=True)
        Path("src/tasks").mkdir(parents=True)
        
        self._write_file("main.py", "# Put everything together\n")
        self._write_file("config.yaml", "# Write all your configs here\n")  # Fixed: added extension
        self._write_file("src/core/__init__.py", "")
        self._write_file("src/core/base_task.py", "# Base class for all automation tasks\n")
        self._write_file("src/core/scheduler.py", "# Task scheduler or job handler\n")
        self._write_file("src/core/executor.py", "# Logic for running or chaining tasks\n")
    
    def vanilla_structure(self):
        """All vanilla file structure creation 
        
        Args: 
            None
            
        Returns:
            Complete vanilla file structure"""
        
        Path(self.name).mkdir()
        
        self._write_file(f"{self.name}/__init__.py", "")
        self._write_file(f"{self.name}/core.py", "# Core functions or classes\n")
        self._write_file(f"{self.name}/utils.py", "# Helper functions\n")
        self._write_file("main.py", "# main entry point of the code\n")