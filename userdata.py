
import string,random
import pyperclip


class UserData:
    '''
    Class that is creates and save new objects of user acccounts data
    '''
    users_list=[]
    password_list = []

    def __init__(self, user_identity, data_identity, account_name, account_key):
        '''
        Initializing the variables for the list of user data
        '''
        self.user_identity=user_identity
        self.data_identity=data_identity
        self.account_name=account_name
        self.account_key=account_key

    def save_account(self):
        '''
        Function to create  and save new accounts n user data list
        '''
        UserData.users_list.append(self)


