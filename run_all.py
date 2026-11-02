"""Runs all notebooks (01, 02, ...) in order and saves their outputs inside each notebook.
Usage:  python run_all.py          (equivalent to opening each notebook and choosing 'Run All')"""
import subprocess, sys, time
from pathlib import Path

for nb in sorted((Path(__file__).resolve().parent / "notebooks").glob("[0-9][0-9]*_*.ipynb")):
    t = time.time(); print(f"Running {nb.name} ...", flush=True)
    subprocess.run([sys.executable, "-m", "jupyter", "nbconvert", "--to", "notebook", "--execute",
                    "--inplace", "--ExecutePreprocessor.timeout=1200", str(nb)],
                   check=True, cwd=nb.parent, stderr=subprocess.DEVNULL)
    print(f"   done in {time.time() - t:.0f} s")
print("\nTables in results/tables, figures in results/figures and results/manuscript_figures")
