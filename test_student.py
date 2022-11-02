import unittest
from student import Student


class TestStudent(unittest.TestCase):

    def test_full_name(self):
        student = Student('Mihai', 'Elisei')
        self.assertEqual(student.full_name, 'Mihai Elisei')





if __name__ == '__main__':
    unittest.main()