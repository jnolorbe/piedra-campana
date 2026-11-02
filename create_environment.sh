#!/usr/bin/env bash
# Creates the Python environment "piedra-campana" with the libraries pinned in requirements.txt.
# Usage (terminal):   cd piedra-campana && bash create_environment.sh
#
#  - With miniforge (mamba/conda): creates the environment named  piedra-campana
#        list with:  conda env list        activate with:  conda activate piedra-campana
#  - Without conda: creates the folder .venv with the prompt name  piedra-campana
#        activate with:  source .venv/bin/activate
set -euo pipefail
cd "$(dirname "$0")"
NAME="piedra-campana"

if command -v mamba >/dev/null 2>&1 || command -v conda >/dev/null 2>&1; then
  CONDA=$(command -v mamba || command -v conda)
  "$CONDA" env create -y -n "$NAME" -f environment.yml
  PY="$("$CONDA" run -n "$NAME" which python)"
  ACT="conda activate $NAME"
elif command -v uv >/dev/null 2>&1; then
  uv venv -p 3.12 --prompt "$NAME" .venv
  VIRTUAL_ENV=.venv uv pip install -r requirements.txt
  PY=.venv/bin/python; ACT="source .venv/bin/activate"
elif command -v python3.12 >/dev/null 2>&1; then
  python3.12 -m venv --prompt "$NAME" .venv
  .venv/bin/python -m pip install --upgrade pip
  .venv/bin/python -m pip install -r requirements.txt
  PY=.venv/bin/python; ACT="source .venv/bin/activate"
else
  echo "Python 3.12 is required (numpy 2.0.2 has no build for 3.13+). Install miniforge or uv (brew install uv)." >&2
  exit 1
fi
"$PY" -c "import numpy, sklearn, librosa; print('Environment \"$NAME\" ready: numpy', numpy.__version__, '| scikit-learn', sklearn.__version__, '| librosa', librosa.__version__)"
echo "Activate with:   $ACT"
echo "Run everything:  python run_all.py"
