import os
import subprocess
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.dirname(BASE_DIR)
ticker_dir = os.path.join(PARENT_DIR, "src_ipynb")

tickers = ["mbb", "vcb", "vcg", "nvl", "fpt"]

# Convert .ipynb to .py
for file in os.listdir(ticker_dir):
    if file.endswith(".ipynb"):
        ipynb_path = os.path.join(ticker_dir, file)
        print(f"Converting: {file}")
        subprocess.run([
            sys.executable, "-m", "nbconvert", "--to", "script", ipynb_path
        ])

        # Rename converted .py file
        py_old = ipynb_path.replace(".ipynb", ".py")
        name_only = file.replace("crawl_", "").replace(".ipynb", "")
        py_new = os.path.join(ticker_dir, f"{name_only}.py")
        if os.path.exists(py_old):
            os.rename(py_old, py_new)

# Run each .py script using the same Python interpreter in virtual environment
for ticker in tickers:
    script_path = os.path.join(ticker_dir, f"{ticker}.py")
    print(f"Running: {script_path}")
    subprocess.run([sys.executable, script_path])
