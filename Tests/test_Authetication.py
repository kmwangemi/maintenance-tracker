
import unittest

class TestPlanner(unittest.TestCase):


    def setUp(self):

        self.user1 = self.create_user('Kelvin', 'Mwangemi', 'Musululiza',
                              '1234', 'mwangemik@gmail.com')


        self.user2 = self.create_user('Okello', 'jackson', 'okello', 'admin', 'okeloo_admin@google.com')
    def test_create_user_success(self):
        """Test a user is created successfully"""
        # self.create_user('Judy', 'Herbert', 'bruno', '1234', 'silverjimmy2@gmail.com')
        self.assertEqual(len(self.user), 2,
                         msg="Length of the the users dictionary should be 4")
    def test_create_user_fail(self):
        """Test failure due to duplicate username"""
        # user1 = self.plan.create_user(self.user)
        user2 = self.create_user('Bruno',
                                      'Herbert',
                                      'bruno',
                                      '1234',
                                      'silverjimmy2@gmail.com')
        self.assertEqual([self.user1, user2], ['Success', 'Fail'])

    def test_login_user_success(self):
        online_before = len(loged_in)
        self.login_user('okello', 'admin')
        online_after = len(loged_in)
        self.assertEqual(online_after, online_before + 1)

if __name__ == '__main__':
    unittest.main()
