import os
import glob
import subprocess
import shutil
import sys

# ---------- CONFIG ----------
# Automatically detect repo directory (where this script resides)
repo_dir = os.path.dirname(os.path.abspath(__file__))

# Binaries folder
binary_dir = os.path.join(repo_dir, "binaries")
os.makedirs(binary_dir, exist_ok=True)

# ---------- FIND LATEST AURORA SCRIPT ----------
py_files = glob.glob(os.path.join(repo_dir, "ADC_Aur_*.py"))

if not py_files:
    print("No Aurora scripts found in the repo root!")
    sys.exit(1)


def version_key(filepath):
    filename = os.path.basename(filepath)
    parts = filename.replace("ADC_Aur_", "").replace(".py", "").split(".")
    return [int(p) for p in parts]


latest_script = max(py_files, key=version_key)
filename = os.path.basename(latest_script)
version = filename.replace("ADC_Aur_", "").replace(".py", "")

binary_path = os.path.join(
    binary_dir, f"ADC_Aur_{version}" + (".exe" if os.name == "nt" else "")
)

# ---------- COMPILE WITH NUITKA ----------
if not os.path.exists(binary_path):
    print(f"Compiling {filename} -> {binary_path}")

    cmd = [
        sys.executable,  # use the current Python interpreter
        "-m",
        "nuitka",
        "--plugin-enable=tk-inter",
        "--onefile",
        "--follow-imports",
        "--output-dir=" + binary_dir,
        latest_script,
    ]

    # Windows-specific options
    if os.name == "nt":
        icon_path = os.path.join(repo_dir, "img", "ico", "ADCIcon.ico")
        if os.path.exists(icon_path):
            cmd.append(f"--windows-icon-from-ico={icon_path}")

    # Debug print of the command
    print("Running command:")
    print(" ".join(cmd))

    subprocess.run(cmd, check=True)

    # ---------- CLEANUP TEMPORARY FOLDERS ----------
    for temp_suffix in [".dist", ".build", ".onefile-build"]:
        temp_dir = os.path.join(binary_dir, f"ADC_Aur_{version}{temp_suffix}")
        if os.path.exists(temp_dir):
            shutil.rmtree(temp_dir)
            print(f"Deleted temporary folder: {temp_dir}")

else:
    print(f"Binary for version {version} already exists. Nothing to do.")

print("Done.")
input("Press Enter to exit...")
