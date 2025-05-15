# -*- coding: utf-8 -*-
"""
Created on Thu Apr  3 19:40:36 2025

@author: Utilizador
"""

from classes.gclass import Gclass

class Member(Gclass):
    
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    # Attribute names list, identifier attribute must be the first one and callled 'id'
    att = ['_member_id','_name','_email','_membership_type','_country']
    # Class header title
    header = 'Members'
    # field description for use in, for example, input form
    des = ['Member id','Name','Email','Membership type','Country']
    
    
    def __init__(self, member_id, name, email, membership_type, country):
        super().__init__()
        
        member_id = Member.get_id(member_id)
        self._member_id = member_id
        self._name = name
        self._email = email
        self._membership_type = membership_type
        self._country = country
        
        Member.obj[member_id] = self
        # Add the id to the list of object ids
        Member.lst.append(member_id)
        
        
    @property
    def member_id(self):
        return self._member_id
    @member_id.setter
    def member_id(self, member_id):
        self._member_id = member_id
        
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        self._name = name
        
    @property
    def email(self):
        return self._email
    @email.setter
    def email(self, email):
        self._email = email
        
    @property
    def membership_type(self):
        return self._membership_type
    @membership_type.setter
    def membership_type(self, membership_type):
        self._membership_type = membership_type


    @property
    def country(self):
        return self._country
    @country.setter
    def country(self, country):
        self._country = country        
        
        