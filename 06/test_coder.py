from coder import Coder
import unittest


class CoderTestCase(unittest.TestCase):
    def setUp(self):
        self.c = Coder('jack')

    def test_skill_in(self):
        c.mastering_skill('java')
        c.mastering_skill('python')
        self.assertIn('java', c.skills)


if __name__ == '__main__':
    unittest.main()
