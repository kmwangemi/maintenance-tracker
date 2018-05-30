
import unittest

class TestUser(unittest.TestCase):
    """Tests for methods in the user"""

    def setUp(self):
        """Setting up a user to use for each test"""
        self.myuser = User('Bruno',
                           'Herbert',
                           'bruno',
                           '1234',
                           'silverjimmy2@gmail.com')

    def test_create_requestlist_success(self):
        """Testing whether a requestlist was successfully created,
        it should increase the length of self.requestlists"""
        count_before = len(self.myuser.request)
        self.myuser.create_request('repair',
                                      'Have a dead motherboard')
        count_after = len(self.myuser.request)
        self.assertEqual(count_after, count_before + 1,
                         msg='count_after should equal count_before + 1')

    def test_create_requestlist_non_string_input(self):
        """Method should raise a type error for non string inputs"""
        self.assertRaises(TypeError,
                          self.myuser.create_request,
                          'has 2 issues', 2,
                          msg="Method only accept string inputs")

    def test_view_requestlists_success(self):
        """View_requestlists should return a list"""
        requestlist = self.myuser.view_request()
        self.assertIsInstance(requestlist, list)

if __name__ == '__main__':
    unittest.main()
