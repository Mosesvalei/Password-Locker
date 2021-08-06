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

 
