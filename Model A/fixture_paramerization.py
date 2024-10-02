import pytest

@pytest.fixture(params=[{"key": "value1"}, {"key": "value2"}])
def test_config(request):
	return request.param

def test_something(test_config):
	assert test_config["key"] in ["value1", "value2"]
