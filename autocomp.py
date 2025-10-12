import os
import glob
import subprocess
import shutil

# Repo and binaries directories
repo_dir = r"D:\Github Git Repo clones\ADC"
binary_dir = os.path.join(repo_dir, "binaries")
os.makedirs(binary_dir, exist_ok=True)

# Find all Aurora scripts in the root of the repo
py_files = glob.glob(os.path.join(repo_dir, "ADC_Aur_*.py"))


# Function to sort versions correctly
def version_key(filepath):
    filename = os.path.basename(filepath)
    parts = filename.replace("ADC_Aur_", "").replace(".py", "").split(".")
    return [int(p) for p in parts]


# Select the latest script
latest_script = max(py_files, key=version_key)
filename = os.path.basename(latest_script)
version = filename.replace("ADC_Aur_", "").replace(".py", "")

# Determine the binary path
binary_path = os.path.join(
    binary_dir, f"ADC_Aur_{version}" + (".exe" if os.name == "nt" else "")
)

if not os.path.exists(binary_path):
    print(f"Compiling {filename} -> {binary_path}")

    cmd = [
        "python",
        "-m",
        "nuitka",
        "--onefile",
        "--follow-imports",
        "--output-dir=" + binary_dir,
        latest_script,
    ]

    if os.name == "nt":
        cmd.append("--plugin-enable=tk-inter")
        cmd.append(
            "--windows-icon-from-ico="
            + os.path.join(repo_dir, "img", "ico", "ADCIcon.ico")
        )

    subprocess.run(cmd, check=True)

    # Cleanup temporary Nuitka folders
    for temp_suffix in [".dist", ".build", ".onefile-build"]:
        temp_dir = os.path.join(binary_dir, f"ADC_Aur_{version}{temp_suffix}")
        if os.path.exists(temp_dir):
            shutil.rmtree(temp_dir)
            print(f"Deleted temporary folder: {temp_dir}")

else:
    print(f"Binary for version {version} already exists. Nothing to do.")

print("Done.")

input("Press Enter to exit...")
