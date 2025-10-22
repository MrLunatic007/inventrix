"""
Inventrix - Intelligent Project Scaffolding and Compilation Tool
"""

import argparse
import sys
from core.creation import Creator
from core.project_management import ComPy  # Import from your project_management.py file

def validate_project_name(name: str) -> bool:
    """
    Validate project name for invalid characters
    
    Args:
        name: Project name to validate
        
    Returns:
        True if valid, False otherwise
    """
    invalid_chars = '<>:"/\\|?*'
    if any(char in name for char in invalid_chars):
        print(f"Error: Project name contains invalid characters: {invalid_chars}")
        return False
    if not name or name.isspace():
        print("Error: Project name cannot be empty")
        return False
    return True

def main():
    """
    The main entry point of Inventrix
    """
    
    parser = argparse.ArgumentParser(
        prog="inventrix",
        description="Intelligent project scaffolding and compiling tool.",
        usage="%(prog)s [command] [options]",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Available Commands:

  --- Project Scaffolding (Inventrix) ---
  init <name> [options]    Initialize a new project from a template.
  list                     List all available project templates.

  --- Project Compilation (ComPy) ---
  compy-init               Initialize ComPy build config (compy.json).
  build                    Build executable using compy.json.
  run                      Build and run executable.
  clean                    Clean build artifacts (dist, build, .spec).
  config                   Show current ComPy configuration.

Examples:
  inventrix init my_new_app -t web-flask
  inventrix list
  
  (After scaffolding, 'cd' into the project)
  cd my_new_app
  inventrix compy-init
  inventrix build
  inventrix run
"""
    )
    
    sub_parser = parser.add_subparsers(
        dest="command",
        help="Available commands",
        required=True
    )
    
    # --- Inventrix Scaffolding Commands ---
    
    # Init command (scaffolding)
    init_command = sub_parser.add_parser(
        "init",
        help="Initialize a new project from a template."
    )
    init_command.add_argument(
        "name",
        type=str,
        help="Project name"
    )
    init_command.add_argument(
        "-t", "--template",
        type=str,
        default="vanilla",
        choices=Creator.VALID_TEMPLATES,  # Use class constant
        help="Template to use for the project"
    )
    init_command.add_argument(
        "-d", "--description",
        type=str,
        default="",
        help="Project description (optional)"
    )
    
    # List templates command
    list_command = sub_parser.add_parser(
        "list",
        help="List all available project templates."
    )
    
    # --- ComPy Compiler Commands ---

    # ComPy Init command
    compy_init_command = sub_parser.add_parser(
        "compy-init",
        help="Initialize ComPy build config (compy.json)"
    )
    
    # Build command
    build_command = sub_parser.add_parser(
        'build',
        help="Build executable using ComPy"
    )
    
    # Run command
    run_command = sub_parser.add_parser(
        'run',
        help="Build and run executable using ComPy"
    )
    
    # Clean command
    clean_command = sub_parser.add_parser(
        'clean',
        help="Clean previous ComPy build artifacts"
    )
    
    # Config command
    config_command = sub_parser.add_parser(
        'config',
        help="Show current ComPy configuration (compy.json)"
    )
    
    
    args = parser.parse_args()
    
    # Instantiate ComPy only if a ComPy command is called
    if args.command in ['compy-init', 'build', 'run', 'clean', 'config']:
        compy = ComPy()
    
    # --- Command Logic ---
    
    if args.command == "init":
        name = args.name
        template = args.template
        
        # Validate project name
        if not validate_project_name(name):
            sys.exit(1)
        
        # Get description if not provided
        if hasattr(args, 'description') and args.description:
            description = args.description
        else:
            description = input("Description (optional): ").strip()
            if not description:
                description = f"A {template} project created with Inventrix"
        
        try:
            print(f"\n🚀 Creating {template} project: {name}")
            print(f"📝 Description: {description}\n")
            
            creator = Creator(name=name, template=template, description=description)
            creator.creating_project_structure()
            
            print(f"\n✅ Project '{name}' created successfully!")
            print(f"📁 Location: ./{name}/")
            print(f"\n💡 Next steps:")
            print(f"   cd {name}")
            print(f"   Check README.md for setup instructions")
            
        except Exception as e:
            print(f"\n❌ Error creating project: {e}")
            sys.exit(1)
            
    elif args.command == "list":
        print("\n📋 Available templates:\n")
        for template in Creator.VALID_TEMPLATES:
            # Add descriptions for each template
            descriptions = {
                "web-django": "Full-stack web framework with Django",
                "web-flask": "Lightweight web framework with Flask",
                "web-streamlit": "Interactive data apps with Streamlit",
                "ml-tensorflow": "Machine learning with TensorFlow",
                "ml-torch": "Machine learning with PyTorch",
                "simulation": "Simulation framework",
                "automation": "Automation script framework",
                "vanilla": "Basic Python project structure"
            }
            desc = descriptions.get(template, "")
            print(f"   • {template:<20} - {desc}")
        print()
    
    # --- ComPy Command Logic ---
        
    elif args.command == "compy-init":
        print("🚀 Initializing ComPy configuration...")
        compy.init_project(args)

    elif args.command == "build":
        compy.build(args)

    elif args.command == "run":
        compy.run(args)

    elif args.command == "clean":
        compy.clean(args)

    elif args.command == "config":
        compy.show_config(args)
        
    else:
        # This branch is technically unreachable if subparsers are `required=True`
        parser.print_help()

if __name__ == "__main__":
    main()