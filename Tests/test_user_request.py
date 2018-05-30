
import unittest

class Testrequestlist(unittest.TestCase):

    def setUp(self):
        self.myrequestlist = request('repair',
                                       'description')
        self.myactivity = Activity("repair", "Having a dead motherboard")

    def test_add_activity_success(self):
        """Tests whether an activity was added to a request """
        self.myrequestlist.add_activity(self.myactivity)
        self.assertIn(self.myactivity, self.myrequestlist.activities,
                      msg="activity should be in list activities of the requestlist object")

    def test_add_activity_string_input(self):
        """add_activity should raise type error with non activity objects"""
        self.assertRaises(TypeError, self.myrequest.add_activity,
                          'activity name',
                          msg="Input should activity object")

    def test_add_activity_integer_input(self):
        """add_activity should raise type error with non activity objects"""
        self.assertRaises(TypeError, self.myrequestlist.add_activity,
                          'activity name', msg="Input should activity object")

    def test_remove_activity_success(self):
        """Test whether activity is removed"""
        self.myrequestlist.add_activity(self.myactivity)
        self.myrequestlist.remove_activity('1')
        self.assertNotIn(self.myrequestlist, self.myrequestlist.activities)

    def test_remove_activity_non_existant(self):
        """Test with an activity that does not exist"""
        status = self.myrequestlist.remove_activity('2')
        self.assertEqual(status, 'Activity does not exist')

    def test_remove_activity_non_string(self):
        """remove_activity should Raise a typeerror if passed a non string"""
        self.assertRaises(TypeError, self.myrequestlist.remove_activity,
                          57, msg="Activity name should be a string")

if __name__ == '__main__':
    unittest.main()
