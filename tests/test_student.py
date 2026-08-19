import pytest
from datetime import date
import random
from unittest.mock import Mock
from src.student import Student

def test_constructor_without_best_friend():
    s = Student(1, "Alice", date(2025, 1, 1))
    assert s.get_name() == "Alice" # Bob should fail, Alice should pass

# --- Comprehensive Tests (Added for >90% Coverage) ---

def test_constructor_with_best_friend():
    friend = Student(2, "Charlie", date(2024, 5, 5))
    s = Student(1, "Alice", date(2025, 1, 1), friend)
    assert s.get_friend() == friend
    assert s.get_friend().get_name() == "Charlie"

def test_getters_and_setters():
    s = Student(1, "Alice", date(2025, 1, 1))
    s.set_id(99)
    s.set_name("Alicia")
    s.set_birthday(date(2026, 2, 2))
    
    assert s.get_id() == 99
    assert s.get_name() == "Alicia"
    assert s.get_birthday() == date(2026, 2, 2)

def test_equals_and_hashcode():
    s1 = Student(1, "Alice", date(2025, 1, 1))
    s2 = Student(1, "Alice", date(2025, 1, 1))
    s3 = Student(2, "Bob", date(2024, 1, 1))
    
    assert s1 == s2
    assert s1 != s3
    assert s1 != None
    assert hash(s1) == hash(s2)
    assert hash(s1) != hash(s3)

def test_comparators():
    s1 = Student(1, "Alice", date(2025, 1, 1))
    s2 = Student(2, "Zack", date(2024, 1, 1))
    
    # Alice comes before Zack alphabetically (negative int)
    assert Student.compare_by_name(s1, s2) < 0
    
    # 2025 comes after 2024 chronologically (positive int)
    assert Student.compare_by_birthday(s1, s2) > 0

def test_to_string():
    friend = Student(2, "Charlie", date(2024, 5, 5))
    s1 = Student(1, "Alice", date(2025, 1, 1), friend)
    s2 = Student(3, "Bob", date(2025, 1, 1))
    
    assert "friend = Charlie" in str(s1)
    assert "friend = no best friend" in str(s2)

def test_assign_random_username_with_mock():
    s = Student(1, "Alice", date(2025, 1, 1))
    
    # Mocking the random object to strictly control the output
    mock_random = Mock(spec=random.Random)
    # Force randint to return 5 for length, then specific indices for characters
    mock_random.randint.side_effect = [5, 0, 1, 2, 3, 4] 
    
    s.assign_random_username(mock_random)
    
    # Based on the mocked indices, it should pick the first 5 chars: "ABCDE"
    assert s.get_name() == "ABCDE"