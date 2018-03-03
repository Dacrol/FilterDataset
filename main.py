# Imports a list of attributes, returns the filenames that match (or doesn't match) the selected attributes.

import os
import numpy as np


class Filterer:
    def __init__(self, attributes=(), attributes_file=os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'attributes.txt'))):
        self.attributes = attributes
        self.filenames = np.array([], dtype='str')
        self.attributes_file = attributes_file
        self.matches = 0

    def get_filenames(self, attributes=()):
        with open(self.attributes_file, mode='rt') as file:
            next(file)
            possible_attributes = file.readline().strip()
        possible_attributes = possible_attributes.split(' ')
        # print(str(possible_attributes))

        if (attributes == () and self.attributes != ()):
            attributes = self.attributes
        filenames = np.loadtxt(self.attributes_file,
                               dtype=str, skiprows=1, usecols=attributes)
        return filenames

    def get_batch(self, no=64):
        return 0
