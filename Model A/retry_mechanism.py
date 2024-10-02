import pytest
import random
from pytest_retry import retry

@retry(max_trials=3, delay=2)
def test_flaky_api_call():
	# Simulate a flaky API call
	response = random.choice([True, False])
	assert response is True
