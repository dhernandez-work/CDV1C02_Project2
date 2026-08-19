"""This module defines the ClassGroup class."""
from src.student import Student

class ClassGroup:
    """Represents a group of students with a maximum capacity."""

    def __init__(self, capacity: int):
        """Initializes the ClassGroup with a given capacity."""
        self._capacity = capacity
        self._students = [None] * capacity
        self._size = 0

    def add_student(self, student: Student) -> bool:
        """Adds a student to the class group."""
        if self._size >= self._capacity:
            return False
        self._students[self._size] = student
        self._size += 1
        return True

    def _find_student_index(self, student_id: int) -> int:
        """Helper method to find a student's index by ID."""
        for i in range(self._size):
            if self._students[i].get_id() == student_id:
                return i
        return -1

    def remove_student(self, student_id: int) -> bool:
        """Removes a student from the class group by their ID."""
        index = self._find_student_index(student_id)
        
        if index == -1:
            return False
            
        for j in range(index, self._size - 1):
            self._students[j] = self._students[j + 1]

        self._students[self._size - 1] = None
        self._size -= 1
        return True

    def get_the_oldest_student(self) -> Student:
        """Returns the oldest student in the class group."""
        if self._size == 0:
            return None

        oldest = self._students[0]
        for i in range(1, self._size):
            if self._students[i].get_birthday() < oldest.get_birthday():
                oldest = self._students[i]

        return oldest

    def get_capacity(self) -> int:
        """Returns the maximum capacity of the class group."""
        return self._capacity

    def get_size(self) -> int:
        """Returns the current number of students in the class group."""
        return self._size

    def get_students(self) -> list:
        """Returns the list of students in the class group."""
        return self._students