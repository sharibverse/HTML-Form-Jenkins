
import unittest

class TestHTMLForm(unittest.TestCase):

    def test_form_fields(self):
        with open("index.html", encoding="utf-8") as f:
            html = f.read()

        self.assertIn("<form", html)
        self.assertIn('name="name"', html)
        self.assertIn('name="email"', html)
        self.assertIn('name="contact"', html)
        self.assertIn('type="submit"', html)

if __name__ == "__main__":
    unittest.main()
