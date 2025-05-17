# -*- coding: utf-8 -*-
"""
Created on Thu Apr  3 19:40:39 2025

@author: Utilizador
"""


from parte_2.classes.gclass import Gclass

class Requisition(Gclass):

    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    # Attribute names list, identifier attribute must be the first one and callled 'id'
    att = ['_member_id', '_book_id', '_borrow_date', '_return_date']
    # Class header title
    header = 'Requisitions'
    # field description for use in, for example, input form
    des = ['Member id', 'Book id', 'Borrow date', 'Return date']


    def __init__(self, member_id, book_id, borrow_date, return_date):
        super().__init__()

        # member_id = Requisition.get_id(member_id)
        # self._member_id = member_id

        # try:
        #     self._member_id = int(member_id)
        # except ValueError:
        #     self._member_id = member_id
        self._member_id = member_id
        self._book_id = book_id
        self._borrow_date = borrow_date
        self._return_date = return_date

        Requisition.obj[member_id] = self
        # Add the id to the list of object ids
        Requisition.lst.append(member_id)

    @property
    def member_id(self):
        return self._member_id
    @member_id.setter
    def member_id(self, member_id):
        self._member_id = member_id

    @property
    def borrow_date(self):
        return self._borrow_date
    @borrow_date.setter
    def borrow_date(self, borrow_date):
        self._borrow_date = borrow_date

    @property
    def book_id(self):
        return self._book_id
    @book_id.setter
    def book_id(self, book_id):
        self._book_id = book_id

    @property
    def return_date(self):
        return self._return_date
    @return_date.setter
    def return_date(self, return_date):
        self._return_date = return_date