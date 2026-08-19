from src.student import Student

class ClassGroup:

    def __init__(self, capacity: int):
        self._capacity = capacity
        self._students = [None] * capacity
        self._size = 0

    def add_student(self, student: Student) -> bool:
        if self._size >= self._capacity: return False
        self._students[self._size] = student
        self._size += 1
        return True

    def remove_student(self, student_id: int) -> bool:
        for i in range(self._size):
            if self._students[i].get_id() == student_id:
                for j in range(i, self._size - 1):
                    self._students[j] = self._students[j + 1]
                
                self._students[self._size - 1] = None
                self._size -= 1
                return True
        
        return False

    def get_the_oldest_student(self) -> Student:
        if self._size == 0: return None

        oldest = self._students[0]
        for i in range(1, self._size):
            if self._students[i].get_birthday() < oldest.get_birthday():
                oldest = self._students[i]
        
        return oldest

    def get_capacity(self) -> int:
        return self._capacity

    def get_size(self) -> int:
        return self._size

    def get_students(self) -> list:
        return self._students