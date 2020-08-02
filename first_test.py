import pytest

def function(x):
	return x + 5

# test function

def test_method():

	x = 3

	result = function(x)

	assert result == 5


# after that run in command line :
# pytest your_file_name.py