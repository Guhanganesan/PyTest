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

# Fixtures

Fixtures are functions, which will run before each test function to which it is applied.

# Conftest

Define fixture in conftest.py file then use across various files

# Xfail and Skip

A test is not relevant for some time due to some reasons.
A new feature is being implemented and we already added a test for that feature.
In these situations, we have the option to xfail the test or skip the tests.

# How to stop the execution of the test after one failure?

pytest test_failure.py -v --maxfail=1

# How to run test in parallel to avoid execution of times

=> pip install pytest-xdist
=> pytest -n 3








