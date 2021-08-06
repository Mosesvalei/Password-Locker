from userdata import UserData
import unittest,pyperclip

class TestUserData(unittest.TestCase):
    '''
    This is a test class that tests cases for creating and authenticating user data
    '''

    def setUp(self):
        '''
        Function to set initial variables for testing
        '''
        self.new_userdata= UserData(1,1,"Yelp","adminpass")

    def tearDown(self):
        '''
        tear down function does clean up after each test case
        '''
        UserData.users_list = []

    def test_init(self):
        '''
        test_init test case to check if objects initialized properly
        '''
        self.assertEqual(self.new_userdata.user_identity,1)
        self.assertEqual(self.new_userdata.data_identity,1)
        self.assertEqual(self.new_userdata.account_name,"Yelp")
        self.assertEqual(self.new_userdata.account_key,"adminpass")

    def test_save_account(self):
        '''
        test_save_account test case to test if userdata object is saved into users_list
        '''
        self.new_userdata.save_account()   #create and save new_cred
        self.assertEqual(len(UserData.users_list),1)


