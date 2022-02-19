#!/usr/bin/env python3
from contact import Contact
# functions that implement the behaviours we have created
def create_contact(fname,lname,phone,email):
    '''
    Function to create a new contact
    '''
    new_contact = Contact(fname,lname,phone,email)
    return new_contact
def save_contacts(contact):
    '''
    Function to save contact
    '''
    contact.save_contact()