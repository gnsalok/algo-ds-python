import unittest
import program


class TestSum(unittest.TestCase):
    def testCase1(self):
        self.assertEqual(program.addTwoNumbers(12,13), 25, "Should be 25")



if __name__ == '__main__':
    unittest.main()