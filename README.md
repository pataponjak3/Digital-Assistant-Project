# Digital-Assistant-Project
Digital Assistant to be developed for the Project of the Bachelor in Computer Science from ISEL

# Utilizing the Digital Assistant
venv\Scripts\activate
pip install -r requirements.txt
python -m src.core.main
deactivate


# Python version
Python 3.10

# Run tests
pytest tests/test_performance.py::(specific test) --log-file=tests/logs/(specific name).log --log-file-level=DEBUG -v