#!/usr/bin/env python
from credentials import Credential
from userdata import UserData
import pyperclip
import string,random,time

#Functions for Credentials
def create_credential(identity, user_name, password):
    '''
    Function used to initialize and create new accounts
    '''
    new_cred = Credential(identity, user_name,password)
    return new_cred


def save_credential(credential):
    '''
    Function that saves user credentials
    '''
    credential.save_credential()

def authenticate(name,password):
    '''
    Function that authenticates for signing in
    '''
    return Credential.authenticate_credential(name,password)

#Functions for User Data
def create_data(user_identity, data_identity, account_name, account_key):
    '''
    Function used to create new user data
    '''
    new_userdata = UserData(user_identity, data_identity, account_name, account_key)
    return new_userdata

def save_account(data):
    '''
    '''
    data.save_account()

def generate_password(length):
    '''
    Function that generates new password
    '''
    return UserData.password_generator(length)

def cred_data_exists(number):
    '''
    Functionthat checks for existing credentials
    '''
    return Credential.cred_data_exists(number)

def data_exists(number):
    '''
    Function that checks if the data exists
    '''
    return UserData.data_exists(number)

def display_data(user_number,data_number):
    '''
    Function that displays existing data
    '''
    return UserData.display_data(user_number,data_number)

def account_exist(name):
    '''
    Function that checks if the account exists by name
    '''
    return UserData.account_exist(name)

def copy_password(number,count):
    '''
    Function that copies the password to the clipboard
    '''
    UserData.copy_password(number,count)


