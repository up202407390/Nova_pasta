# -*- coding: utf-8 -*-
"""
Created on Thu Apr  3 19:40:38 2025

@author: Utilizador
"""


from classes.gclass import Gclass

class Publisher(Gclass):

    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    # Attribute names list, identifier attribute must be the first one and callled 'id'
    att = ['_id', '_publisher_name', '_country']
    # Class header title
    header = 'Publishers'
    # field description for use in, for example, input form
    des = ['Publisher id', 'Publisher name', 'Country']


    def __init__(self, _id, publisher_name, country):
        super().__init__()

        _id = Publisher.get_id(_id)
        self.__id = _id
        self._publisher_name = publisher_name
        self._country = country

        Publisher.obj[_id] = self
        # Add the id to the list of object ids
        Publisher.lst.append(_id)

    @property
    def publisher_id(self):
        return self._publisher_id
    @publisher_id.setter
    def publisher_id(self, _id):
        self.__id = _id

    @property
    def publisher_name(self):
        return self._publisher_name
    @publisher_name.setter
    def publisher_name(self, publisher_name):
        self._publisher_name = publisher_name

    @property
    def country(self):
        return self._country
    @country.setter
    def country(self, country):
        self._country = country

