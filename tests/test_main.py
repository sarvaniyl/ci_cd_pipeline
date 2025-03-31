import unittest
from app.main import hello_world, sub

class TestMain(unittest.TestCase):
    def test_hello_world(self):
        self.assertEqual(hello_world(), "Hello, Docker and GitHub Actions!")
    
    def test_sub(self):
        self.assertEqual(sub(10, 8), 2)
        self.assertEqual(sub(-1, -1), 0)
        self.assertEqual(sub(-8, 3), -11)

if __name__ == "__main__":
    unittest.main()