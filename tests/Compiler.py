import os
import platform
import subprocess
import sys

def compile_to_executable(script_path):
    if not os.path.exists(script_path):
        print(f"The file '{script_path}' does not exist.")
        return

    # Determine the operating system
    current_os = platform.system()
    if current_os == "Windows":
        ext = ".exe"
    else:
        ext = ""  # Linux does not require an extension

    # Prepare the output
    output_dir = os.path.join(os.path.dirname(script_path), "dist")
    output_name = os.path.splitext(os.path.basename(script_path))[0] + ext

    # Create the PyInstaller command
    command = [
        "pyinstaller",
        "--onefile",             # Single executable file
        "--name", output_name,  # Output name
        "--distpath", output_dir, # Output directory
        script_path              # Input file
    ]

    # Execute the command
    try:
        subprocess.run(command, check=True)
        print(f"The file has been compiled to '{os.path.join(output_dir, output_name)}'")
    except subprocess.CalledProcessError as e:
        print("Something went wrong during compilation:", e)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python compile_script.py <script_path>")
    else:
        script_path = sys.argv[1]
        compile_to_executable(script_path)
