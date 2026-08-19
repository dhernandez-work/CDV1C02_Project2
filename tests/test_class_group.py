import pytest
from datetime import date
from src.class_group import ClassGroup
from src.student import Student

def test_constructor():
    capacity = 5
    group = ClassGroup(capacity)
    assert group.get_capacity() == 5 

def test_add_student_success():
    group = ClassGroup(2)
    s1 = Student(1, "Alice", date(2025, 1, 1))
    assert group.add_student(s1) == True
    assert group.get_size() == 1
    assert group.get_students()[0] == s1

def test_add_student_exceeds_capacity():
    group = ClassGroup(1)
    s1 = Student(1, "Alice", date(2025, 1, 1))
    s2 = Student(2, "Bob", date(2024, 1, 1))
    assert group.add_student(s1) == True
    assert group.add_student(s2) == False
    assert group.get_size() == 1

def test_remove_student_success():
    group = ClassGroup(3)
    s1 = Student(1, "Alice", date(2025, 1, 1))
    s2 = Student(2, "Bob", date(2024, 1, 1))
    group.add_student(s1)
    group.add_student(s2)
    assert group.remove_student(1) == True
    assert group.get_size() == 1
    assert group.get_students()[0].get_name() == "Bob"
    assert group.get_students()[1] is None

def test_remove_student_not_found():
    group = ClassGroup(2)
    s1 = Student(1, "Alice", date(2025, 1, 1))
    group.add_student(s1)
    assert group.remove_student(99) == False
    assert group.get_size() == 1

def test_get_oldest_student():
    group = ClassGroup(3)
    s1 = Student(1, "Alice", date(2025, 1, 1))
    s2 = Student(2, "Bob", date(2020, 1, 1)) 
    s3 = Student(3, "Charlie", date(2022, 1, 1))
    group.add_student(s1)
    group.add_student(s2)
    group.add_student(s3)
    assert group.get_the_oldest_student().get_name() == "Bob"

def test_get_oldest_student_empty_group():
    group = ClassGroup(2)
    assert group.get_the_oldest_student() is None

def test_remove_last_student():
    # Edge Case: Safely removing the final student in the array
    group = ClassGroup(3)
    s1 = Student(1, "Alice", date(2025, 1, 1))
    s2 = Student(2, "Bob", date(2024, 1, 1))
    group.add_student(s1)
    group.add_student(s2)
    assert group.remove_student(2) == True
    assert group.get_size() == 1
    assert group.get_students()[0].get_name() == "Alice"
    assert group.get_students()[1] is None