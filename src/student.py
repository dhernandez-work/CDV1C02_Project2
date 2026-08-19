"""This module defines the Student class."""
from datetime import date
import random

class Student:
    """Represents a student entity with their details."""

    def __init__(self, student_id: int, name: str, birthday: date, friend: 'Student' = None):
        """Initializes a Student with an ID, name, birthday, and an optional best friend."""
        self._id = student_id
        self._name = name
        self._birthday = birthday
        self._friend = friend # can be null if don't have any best friend

    def get_id(self) -> int:
        """Returns the student's ID."""
        return self._id

    def get_name(self) -> str:
        """Returns the student's name."""
        return self._name

    def get_birthday(self) -> date:
        """Returns the student's birthday."""
        return self._birthday

    def get_friend(self) -> 'Student':
        """Returns the student's best friend."""
        return self._friend

    def set_id(self, student_id: int) -> None:
        """Sets the student's ID."""
        self._id = student_id

    def set_name(self, name: str) -> None:
        """Sets the student's name."""
        self._name = name

    def set_birthday(self, birthday: date) -> None:
        """Sets the student's birthday."""
        self._birthday = birthday

    def set_friend(self, friend: 'Student') -> None:
        """Sets the student's best friend."""
        self._friend = friend

    def __eq__(self, o: object) -> bool:
        """Checks if this student is equal to another object."""
        if self is o:
            return True
        if o is None or self.__class__ != o.__class__:
            return False
        return (self._id == o.get_id() and
                self._name == o.get_name() and
                self._birthday == o.get_birthday())

    def __hash__(self) -> int:
        """Returns the hash code for the student."""
        return hash((self._id, self._name, self._birthday))

    @staticmethod
    def compare_by_name(s1: 'Student', s2: 'Student') -> int:
        """Compares two students by their names alphabetically."""
        name1 = s1.get_name().lower()
        name2 = s2.get_name().lower()
        return (name1 > name2) - (name1 < name2)

    @staticmethod
    def compare_by_birthday(s1: 'Student', s2: 'Student') -> int:
        """Compares two students by their birthdays."""
        b1 = s1.get_birthday()
        b2 = s2.get_birthday()
        return (b1 > b2) - (b1 < b2)

    def __str__(self) -> str:
        """Returns a string representation of the student."""
        friend_name = self._friend.get_name() if self._friend else "no best friend"
        return "Student{id = " + str(self._id) + \
               ", name = '" + self._name + '\'' + \
               ", birthday = " + str(self._birthday) + \
               ", friend = " + friend_name + \
               '}'

    def assign_random_username(self, rand: random.Random) -> None:
        """Assigns a random alphanumeric username to the student."""
        min_length = 5
        max_length = 10

        length = rand.randint(min_length, max_length)

        sb = []
        chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789_"

        for _ in range(length):
            sb.append(chars[rand.randint(0, len(chars) - 1)])

        self._name = "".join(sb)
