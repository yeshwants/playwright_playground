# playwright_playground

# Steps to install pyenv on mac
brew install pyenv
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init --path)"
eval "$(pyenv init -)"
pyenv install 3.9.6
python -m venv 396     # this creates a virtual env in this folder if it doesnt have
source 396/bin/activate    # this activates the 3.9.6 virtual env 



# Steps to run the scripts to play with playwright
pip install -r requirements.txt
playwright install chromium
playwright install-deps chromium
python amazon_search.py
