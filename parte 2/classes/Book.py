# -*- coding: utf-8 -*-
"""
Created on Thu Apr  3 19:28:40 2025

@author: Utilizador
"""

from classes.gclass import Gclass

class Book(Gclass):
    
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    # Attribute names list, identifier attribute must be the first one and callled 'id'
    att = ['_book_id','_title','_author','_genre','_publisher_id']
    # Class header title
    header = 'Books'
    # field description for use in, for example, input form
    des = ['Book id','Title','Author','Genre','Publisher id']
    
    
    def __init__(self, book_id, title, author, genre, publisher_id):
        super().__init__()
        
        book_id = Book.get_id(book_id)
        self._book_id = book_id
        self._title = title
        self._author = author
        self._genre = genre
        self._publisher_id = publisher_id
        
        Book.obj[book_id] = self
        # Add the id to the list of object ids
        Book.lst.append(book_id)
        
    @property
    def book_id(self):
        return self._book_id
    
    @property
    def id(self):
        return self._book_id

    
    @book_id.setter
    def book_id(self, book_id):
        self._book_id = book_id
            
    @property
    def title(self):
        return self._title
    @title.setter
    def title(self, title):
        self._title = title
        
    @property
    def author(self):
        return self._author
    @author.setter
    def author(self, author):
        self._author = author
        
    @property
    def genre(self):
        return self._genre
    @genre.setter
    def genre(self, genre):
        self._genre = genre
        
    @property
    def publisher_id(self):
        return self._publisher_id
    @publisher_id.setter
    def publisher_id(self, publisher_id):
        self._publisher_id = publisher_id