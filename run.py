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


