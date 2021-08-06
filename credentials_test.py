from credential import Credential
import unittest

class TestCredential(unittest.TestCase):
    '''
    This is a test class that tests cases for creating and authenticating credentials
    '''

    def setUp(self):
        '''
        Function to set initial variables for testing
        '''
        self.new_cred = Credential(1,"Sophia","admin")

    def tearDown(self):
        '''
        tear down function does clean up after each test case
        '''
        Credential.credential_list = []

    def test_init(self):
        '''
        test_init test case to test if the object initialized properly
        '''
        self.assertEqual(self.new_cred.identity,1)
        self.assertEqual(self.new_cred.user_name,"Sophia")
        self.assertEqual(self.new_cred.password,"admin")


