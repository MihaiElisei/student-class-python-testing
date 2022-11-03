import unittest
from student import Student


class TestStudent(unittest.TestCase):

    def test_full_name(self):
        student = Student('Mihai', 'Elisei')
        self.assertEqual(student.full_name, 'Mihai Elisei')

    def test_alert_santa(self):
        student = Student('Mihai', 'Elisei')
        student.alert_santa()
        
        self.assertTrue(student.naughty_list)

    def test_email(self):
        student = Student('Mihai', 'Elisei')

        self.assertEqual(student.email, 'mihai.elisei@email.com')


if __name__ == '__main__':
    unittest.main()