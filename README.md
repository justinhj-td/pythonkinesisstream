pyenv install 3.9.5
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init --path)"
pyenv local 3.9.5
pip install --upgrade pip
pip install -r requirements.txt

