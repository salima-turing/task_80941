# conftest.py
import pytest
from pytest_isolation import isolation

@pytest.fixture(scope="function")
def isolated_db():
    # Isolate the database for each function-scoped test
    with isolation("db"):
        yield

# test_erp_system.py
from erp_system import Employee, Database
import pytest

@pytest.fixture
def db():
    return Database()

def test_employee_creation(db, isolated_db):
    emp = Employee("Dummy", "Employee", db)
    emp.save()

    # Assertion to check if employee is created successfully
    assert Employee.get_by_id(emp.id, db) is not None

def test_employee_update(db, isolated_db):
    emp = Employee("Dummy", "Employee", db)
    emp.save()

    emp.update_name("Updated Name")

    # Assertion to check if employee name is updated successfully
    updated_emp = Employee.get_by_id(emp.id, db)
    assert updated_emp.name == "Updated Name"
