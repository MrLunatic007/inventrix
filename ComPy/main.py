#!/usr/bin/env python3
"""
ComPy - A simple Python to executable compiler
Usage: python compy.py [command] [options]
"""

import os
import sys
import json
import subprocess
import shutil
import argparse
from pathlib import Path
from typing import Dict, List, Optional

class ComPy:
    def __init__(self):
        self.config_file = "compy.json"
        self.default_config = {
            "name": "app",
            "entry": "main.py",
            "icon": None,
            "onefile": True,
            "console": True,
            "hidden_imports": [],
            "data_files": [],
            "exclude_modules": [],
            "upx": False,
            "clean": True,
            "dist_dir": "dist",
            "build_dir": "build"
        }
        self.config = {}
    
    def check_pyinstaller(self) -> bool:
        """Check if PyInstaller is installed"""
        try:
            subprocess.run(["pyinstaller", "--version"], 
                         capture_output=True, check=True)
            return True
        except (subprocess.CalledProcessError, FileNotFoundError):
            return False
    
    def install_pyinstaller(self):
        """Install PyInstaller"""
        print("📦 PyInstaller not found. Installing...")
        try:
            subprocess.run([sys.executable, "-m", "pip", "install", "pyinstaller"],
                         check=True)
            print("✅ PyInstaller installed successfully!")
        except subprocess.CalledProcessError:
            print("❌ Failed to install PyInstaller. Please install manually:")
            print("   pip install pyinstaller")
            sys.exit(1)
    
    def init_project(self, args):
        """Initialize a new ComPy project"""
        if os.path.exists(self.config_file):
            overwrite = input(f"⚠️  {self.config_file} already exists. Overwrite? (y/N): ")
            if overwrite.lower() != 'y':
                print("❌ Init cancelled.")
                return
        
        config = self.default_config.copy()
        
        # Interactive setup
        print("\n🚀 ComPy Project Setup")
        print("=" * 50)
        
        name = input(f"Project name [{config['name']}]: ").strip()
        if name:
            config['name'] = name
        
        entry = input(f"Entry point [{config['entry']}]: ").strip()
        if entry:
            config['entry'] = entry
        
        icon = input("Icon file (optional, .ico): ").strip()
        if icon:
            config['icon'] = icon
        
        onefile = input("One file executable? (Y/n): ").strip().lower()
        config['onefile'] = onefile != 'n'
        
        console = input("Show console window? (Y/n): ").strip().lower()
        config['console'] = console != 'n'
        
        # Save config
        with open(self.config_file, 'w') as f:
            json.dump(config, f, indent=2)
        
        print(f"\n✅ Created {self.config_file}")
        print(f"📝 Edit this file to customize your build settings")
        print(f"🔨 Run 'python compy.py build' to compile your project")
    
    def load_config(self) -> Dict:
        """Load configuration from compy.json"""
        if not os.path.exists(self.config_file):
            print(f"❌ {self.config_file} not found!")
            print(f"💡 Run 'python compy.py init' to create a project")
            sys.exit(1)
        
        with open(self.config_file, 'r') as f:
            config = json.load(f)
        
        # Merge with defaults
        final_config = self.default_config.copy()
        final_config.update(config)
        return final_config
    
    def build_pyinstaller_command(self, config: Dict) -> List[str]:
        """Build PyInstaller command from config"""
        cmd = ["pyinstaller"]
        
        # Basic options
        if config['onefile']:
            cmd.append("--onefile")
        
        if not config['console']:
            cmd.append("--windowed")
        
        # Name
        cmd.extend(["--name", config['name']])
        
        # Icon
        if config.get('icon'):
            cmd.extend(["--icon", config['icon']])
        
        # Directories
        cmd.extend(["--distpath", config['dist_dir']])
        cmd.extend(["--workpath", config['build_dir']])
        
        # Hidden imports
        for imp in config.get('hidden_imports', []):
            cmd.extend(["--hidden-import", imp])
        
        # Data files
        for data in config.get('data_files', []):
            if isinstance(data, dict):
                src = data.get('src')
                dst = data.get('dst', '.')
                cmd.extend(["--add-data", f"{src}{os.pathsep}{dst}"])
            else:
                cmd.extend(["--add-data", f"{data}{os.pathsep}."])
        
        # Exclude modules
        for mod in config.get('exclude_modules', []):
            cmd.extend(["--exclude-module", mod])
        
        # UPX
        if not config.get('upx', False):
            cmd.append("--noupx")
        
        # Clean
        if config.get('clean', True):
            cmd.append("--clean")
        
        # Entry point
        cmd.append(config['entry'])
        
        return cmd
    
    def build(self, args):
        """Build the executable"""
        # Check PyInstaller
        if not self.check_pyinstaller():
            self.install_pyinstaller()
        
        # Load config
        config = self.load_config()
        
        # Check entry point exists
        if not os.path.exists(config['entry']):
            print(f"❌ Entry point '{config['entry']}' not found!")
            sys.exit(1)
        
        # Build command
        cmd = self.build_pyinstaller_command(config)
        
        print("🔨 Building executable...")
        print(f"📄 Command: {' '.join(cmd)}")
        print("=" * 50)
        
        try:
            # Run PyInstaller
            result = subprocess.run(cmd, check=True)
            
            print("=" * 50)
            print("✅ Build successful!")
            
            # Find executable
            dist_path = Path(config['dist_dir'])
            if config['onefile']:
                exe_name = config['name']
                if sys.platform == 'win32':
                    exe_name += '.exe'
                exe_path = dist_path / exe_name
            else:
                exe_path = dist_path / config['name']
            
            if exe_path.exists():
                print(f"📦 Executable: {exe_path}")
                if not config['onefile']:
                    print(f"📂 Application folder: {exe_path}")
            
        except subprocess.CalledProcessError:
            print("\n❌ Build failed!")
            sys.exit(1)
    
    def clean(self, args):
        """Clean build artifacts"""
        config = self.load_config()
        
        print("🧹 Cleaning build artifacts...")
        
        paths_to_remove = [
            config['build_dir'],
            config['dist_dir'],
            f"{config['name']}.spec"
        ]
        
        for path in paths_to_remove:
            if os.path.exists(path):
                if os.path.isfile(path):
                    os.remove(path)
                    print(f"🗑️  Removed {path}")
                else:
                    shutil.rmtree(path)
                    print(f"🗑️  Removed {path}/")
        
        print("✅ Clean complete!")
    
    def run(self, args):
        """Build and run the executable"""
        self.build(args)
        
        config = self.load_config()
        
        # Determine executable path
        dist_path = Path(config['dist_dir'])
        if config['onefile']:
            exe_name = config['name']
            if sys.platform == 'win32':
                exe_name += '.exe'
            exe_path = dist_path / exe_name
        else:
            exe_name = config['name']
            if sys.platform == 'win32':
                exe_name += '.exe'
            exe_path = dist_path / config['name'] / exe_name
        
        if not exe_path.exists():
            print(f"❌ Executable not found: {exe_path}")
            sys.exit(1)
        
        print(f"\n🚀 Running {exe_path}...")
        print("=" * 50)
        
        try:
            subprocess.run([str(exe_path)])
        except KeyboardInterrupt:
            print("\n\n⚠️  Interrupted")
    
    def show_config(self, args):
        """Show current configuration"""
        config = self.load_config()
        
        print("\n📋 Current ComPy Configuration")
        print("=" * 50)
        print(json.dumps(config, indent=2))
        print("=" * 50)
        print(f"\n📝 Edit {self.config_file} to modify settings")

def main():
    parser = argparse.ArgumentParser(
        description="ComPy - Simple Python to Executable Compiler",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python compy.py init              # Initialize new project
  python compy.py build             # Build executable
  python compy.py run               # Build and run executable
  python compy.py clean             # Clean build artifacts
  python compy.py config            # Show configuration

Config file (compy.json) options:
  name              - Output executable name
  entry             - Main Python file
  icon              - Icon file (.ico)
  onefile           - Single executable (true/false)
  console           - Show console window (true/false)
  hidden_imports    - List of modules to include
  data_files        - List of data files to bundle
  exclude_modules   - List of modules to exclude
  upx               - Use UPX compression (true/false)
  clean             - Clean before build (true/false)
        """
    )
    
    parser.add_argument('command', 
                       choices=['init', 'build', 'run', 'clean', 'config'],
                       help='Command to execute')
    
    args = parser.parse_args()
    
    compy = ComPy()
    
    commands = {
        'init': compy.init_project,
        'build': compy.build,
        'run': compy.run,
        'clean': compy.clean,
        'config': compy.show_config
    }
    
    commands[args.command](args)

if __name__ == "__main__":
    main()