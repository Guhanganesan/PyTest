# PyTest

# Install Pytest
pip install pytest

# File format
Running pytest without mentioning a filename will run all files of format test_*.py or *_test.py in the current directory and subdirectories

# How to run code?

=> pytest
for verbosity
=> pytest -v
=> pytest -vv 

# Matching test names (file names)

Example:
test_greater.py
test_greater_than_equal.py
test_equal.py

=> pytest -k <substring> -v => pytest -k great -v 
=> This will execute which file name has its own name contains "great"


