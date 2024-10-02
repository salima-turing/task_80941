import pytest
import random

# Dummy ERP system class for demonstration
class ERPSystem:
	def __init__(self):
		self.data = []

	def add_record(self, record):
		self.data.append(record)

	def get_records(self):
		return self.data

@pytest.fixture
def erp_system():
	"""
	Set up a fresh ERP system instance for each test.
	"""
	return ERPSystem()

def test_add_record(erp_system):
	# Test with dummy data
	test_data = [
		{"id": 1, "name": "Product A"},
		{"id": 2, "name": "Product B"},
	]

	for record in test_data:
		erp_system.add_record(record)

	records = erp_system.get_records()
	assert len(records) == len(test_data)
	for i in range(len(test_data)):
		assert records[i] == test_data[i]

if __name__ == "__main__":
	pytest.main()
