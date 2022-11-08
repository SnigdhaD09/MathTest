import unittest
import MathOpera


class TestCheck(unittest.TestCase):

    def test_add(self):
        test = MathOpera.MathOperator(5,2,'+')
        self.assertEqual(test, 7)

    def test_sub(self):
        test = MathOpera.MathOperator(5,2,'-')
        self.assertEqual(test, 3)

    def test_multiply(self):
        test = MathOpera.MathOperator(5,2,'*')
        self.assertEqual(test, 10)

    def test_failure(self):
        test = MathOpera.MathOperator(2,2,"/")
        self.assertEqual(test, 'failure')

    from unittest.mock import patch

    @patch('MathOpera.math_addition')
    def test_stub(self, mock_test):
        mock_test.return_value = 20
        test = MathOpera.MathOperator(2,3,"+")
        self.assertEqual(test, 20)


if __name__ == '__main__':
    unittest.main()

