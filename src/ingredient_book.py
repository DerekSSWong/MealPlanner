import pandas as pd
import os

class IngredientBook:

    def __init__(self):
        # check for recipe file and read it as dataframe, generate new dataframe if file is not found
        if os.path.isfile('IngredientBook.csv'):
            print('yes')
        else:
            self.data = pd.DataFrame(columns=['name', 'desc'])
        None
    
    @property
    def data(self):
        return self._data
    
    @data.setter
    def data(self, input):
        self._data = input

    def add_ingredient(self, name, desc):
        # Check for duplicate names, add ingredeient info to dataframe
        self.data.loc[len(self.data)] = {'name': 'name', 'desc': 'test ingredient'}

    def search_ingredients(self, keyword):
        # returns anything that fits the keyword
        None
    def delete_ingredient(self, name):
        # deletes the ingredient of the exact name
        None

    def load_file(self, path):
        # loads the ingredient book file
        None
    def save_file(self, path):
        # saves current ingredient book as csv, replacing existing book file
        None

test = IngredientBook()