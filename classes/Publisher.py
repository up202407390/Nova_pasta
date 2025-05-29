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

    # Correspondência exata com a tabela Publisher
    # publishers_id = INTEGER, publisher_name = TEXT, country = TEXT
    att = ['_publishers_id', '_publisher_name', '_country']
    header = 'Publishers'
    des = ['Publisher ID', 'Publisher Name', 'Country']

    def __init__(self, publishers_id, publisher_name, country):
        super().__init__()
        publishers_id = Publisher.get_id(publishers_id)
        self._publishers_id = publishers_id
        self._publisher_name = publisher_name
        self._country = country

        Publisher.obj[publishers_id] = self
        Publisher.lst.append(publishers_id)

    @property
    def publishers_id(self):
        return self._publishers_id

    @publishers_id.setter
    def publishers_id(self, value):
        self._publishers_id = value

    @property
    def publisher_name(self):
        return self._publisher_name

    @publisher_name.setter
    def publisher_name(self, value):
        self._publisher_name = value

    @property
    def country(self):
        return self._country

    @country.setter
    def country(self, value):
        self._country = value
