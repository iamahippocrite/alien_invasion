currentDirectory=${PWD##*/}
venv="venv"
venvname="$venv$currentDirectory"
echo `pyenv activate $venvname`
