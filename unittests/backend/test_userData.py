from unittest import TestCase
from backend.UserData import UserData


class TestUserData(TestCase):

    # get_input will return 'yes' during this test
    def test_as_line_good(self):
        actual: str
        userData = UserData('testname1', 'testaccount1')
        self.assertIsNotNone(userData)
        actual = userData.as_line()
        self.assertIsNotNone(actual)
        self.assertEqual(actual, 'Users name: testname1 has account: testaccount1')

