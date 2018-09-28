import unittest
from bw_brackets_pa import solution


class TestIfBracketsAreBalanced(unittest.TestCase):
    def testLine1(self):
        self.assertEqual(solution("hello world"), -1)

    def testLine2(self):
        self.assertEqual(solution("{}"), -1)

    def testLine3(self):
        self.assertEqual(solution("{{{foo();}}}{}"), -1)

    def testLine4(self):
        self.assertEqual(solution("{{}{}}"), -1)

    def testLine5(self):
        self.assertEqual(solution("{{{}"), 0)

    def testLine6(self):
        self.assertEqual(solution("}"), 0)

    def testLine7(self):
        self.assertEqual(solution("{}{foo{}"), 2)


if __name__ == "__main__":
    unittest.main()
