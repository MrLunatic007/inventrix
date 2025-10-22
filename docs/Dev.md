<a id="main"></a>

# main

Inventrix - Intelligent Project Scaffolding and Compilation Tool

<a id="main.validate_project_name"></a>

#### validate\_project\_name

```python
def validate_project_name(name: str) -> bool
```

Validate project name for invalid characters

**Arguments**:

- `name` - Project name to validate
  

**Returns**:

  True if valid, False otherwise

<a id="main.main"></a>

#### main

```python
def main()
```

The main entry point of Inventrix

<a id="core.project_management"></a>

# core.project\_management

ComPy - A simple Python to executable compiler
Usage: python compy.py [command] [options]

<a id="core.project_management.ComPy"></a>

## ComPy Objects

```python
class ComPy()
```

<a id="core.project_management.ComPy.check_pyinstaller"></a>

#### check\_pyinstaller

```python
def check_pyinstaller() -> bool
```

Check if PyInstaller is installed

<a id="core.project_management.ComPy.install_pyinstaller"></a>

#### install\_pyinstaller

```python
def install_pyinstaller()
```

Install PyInstaller

<a id="core.project_management.ComPy.init_project"></a>

#### init\_project

```python
def init_project(args)
```

Initialize a new ComPy project

<a id="core.project_management.ComPy.load_config"></a>

#### load\_config

```python
def load_config() -> Dict
```

Load configuration from compy.json

<a id="core.project_management.ComPy.build_pyinstaller_command"></a>

#### build\_pyinstaller\_command

```python
def build_pyinstaller_command(config: Dict) -> List[str]
```

Build PyInstaller command from config

<a id="core.project_management.ComPy.build"></a>

#### build

```python
def build(args)
```

Build the executable

<a id="core.project_management.ComPy.clean"></a>

#### clean

```python
def clean(args)
```

Clean build artifacts

<a id="core.project_management.ComPy.run"></a>

#### run

```python
def run(args)
```

Build and run the executable

<a id="core.project_management.ComPy.show_config"></a>

#### show\_config

```python
def show_config(args)
```

Show current configuration

<a id="core.file_processor"></a>

# core.file\_processor

<a id="core.file_processor.FileProcessor"></a>

## FileProcessor Objects

```python
class FileProcessor()
```

<a id="core.file_processor.FileProcessor.constants"></a>

#### constants

```python
def constants(template)
```

Holds all the constant file contents that should appear in all projects

**Arguments**:

- `template` _str_ - The template type being used
  

**Returns**:

- `dict` - Dictionary containing README and gitignore content

<a id="core.file_processor.FileProcessor.django"></a>

#### django

```python
def django()
```

Contains all the files for the django template

**Arguments**:

  None
  

**Returns**:

  Complete file content for core files in django projects.

<a id="core.file_processor.FileProcessor.flask"></a>

#### flask

```python
def flask()
```

Holds all content for flask templated projects

<a id="core.file_processor.FileProcessor.streamlit"></a>

#### streamlit

```python
def streamlit()
```

streamlit file contents

**Arguments**:

  None
  
  Returns a dict of the file contents

<a id="core.creation"></a>

# core.creation

<a id="core.creation.Creator"></a>

## Creator Objects

```python
class Creator()
```

Responsible for creating the folder and adding files to the folders

**Arguments**:

- `name` _str_ - The project name
- `description` _str_ - The project description
- `template` _str_ - The template type for the project
  

**Returns**:

  A complete file structure with all the files intact and with sample code

<a id="core.creation.Creator.creating_project_structure"></a>

#### creating\_project\_structure

```python
def creating_project_structure()
```

Creates the file structure according to the template selected

**Arguments**:

  None
  

**Returns**:

  A complete file structure as per the template

<a id="core.creation.Creator.python_venv"></a>

#### python\_venv

```python
def python_venv(requirements: str = "requirements.txt")
```

Making a python virtual environment and installs the requirements

**Arguments**:

- `requirements` _str_ - Requirements file path

<a id="core.creation.Creator.django_structure"></a>

#### django\_structure

```python
def django_structure()
```

All django file structure creation

**Arguments**:

  None
  

**Returns**:

  Complete django file structure

<a id="core.creation.Creator.flask_structure"></a>

#### flask\_structure

```python
def flask_structure()
```

All Flask file structure creation

**Arguments**:

  None
  

**Returns**:

  Complete flask structure

<a id="core.creation.Creator.streamlit_structure"></a>

#### streamlit\_structure

```python
def streamlit_structure()
```

All streamlit file structure creation

**Arguments**:

  None
  

**Returns**:

  Complete streamlit structure

<a id="core.creation.Creator.ml_tensorflow_structure"></a>

#### ml\_tensorflow\_structure

```python
def ml_tensorflow_structure()
```

All Machine learning tensorflow file structure creation

**Arguments**:

  None
  

**Returns**:

  Complete tensorflow file structure

<a id="core.creation.Creator.ml_torch_structure"></a>

#### ml\_torch\_structure

```python
def ml_torch_structure()
```

All Machine learning torch file structure creation

**Arguments**:

  None
  

**Returns**:

  Complete torch file structure

<a id="core.creation.Creator.simulation_structure"></a>

#### simulation\_structure

```python
def simulation_structure()
```

All simulation file structure creation

**Arguments**:

  None
  

**Returns**:

  Complete simulation file structure

<a id="core.creation.Creator.automation_structure"></a>

#### automation\_structure

```python
def automation_structure()
```

All automation file structure creation

**Arguments**:

  None
  

**Returns**:

  Complete automation file structure

<a id="core.creation.Creator.vanilla_structure"></a>

#### vanilla\_structure

```python
def vanilla_structure()
```

All vanilla file structure creation

**Arguments**:

  None
  

**Returns**:

  Complete vanilla file structure

