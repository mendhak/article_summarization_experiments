
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
# Extra setup
python -m spacy download en_core_web_sm
python3 -c 'import nltk; nltk.download("punkt")'
# Run tests
python3 main_spacy2.py
python3 main.py
python3 main_newspaper3k.py
```