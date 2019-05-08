import unittest
from . import first


class IntegerArithmeticTestCase(unittest.TestCase):
    def test_first_question(self):  # test method names begin with 'test'
        self.assertEqual(first.first_question('asdf'), True)
        self.assertEqual(first.first_question('asdfa'), False)

    def test_second_question(self):
        self.assertEqual(first.second_question('asdf'), 'fdsa')
        self.assertEqual(first.second_question('as df'), 'fd sa')

    def test_third_question(self):
        self.assertEqual(first.third_question('asdfasdf'), 'asdf')
        self.assertEqual(first.third_question('as df'), 'as df')

    def test_fourth_question(self):
        self.assertEqual(first.fourth_question('asdfasdf', 'asdffdsa'), True)
        self.assertEqual(first.fourth_question('fastt', 'tasf'), False)

    def test_fifth_question(self):
        self.assertEqual(first.fifth_question('as as'), 'as%20as')
        self.assertEqual(first.fifth_question('asdf'), 'asdf')

    def test_sixth_question(self):
        matrix = [
            list(range(5)),
            list(range(5)),
            list(range(5)),
            list(range(5)),
            list(range(5)),
        ]
        self.assertEqual(first.sixth_question(matrix), True)


if __name__ == '__main__':
    unittest.main()
    t = 'asdfasdf'
