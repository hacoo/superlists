from django.test import TestCase # testcase is an augmented version of unittest.


# Create your tests here.

class SmokeTest(TestCase):

    def test_bad_math(self):
        self.assertEqual(1+1, 3)

        

        