# Imports a list of attributes, returns the filenames that match (or doesn't match) the selected attributes.

import os
import numpy as np


class Filterer:
    def __init__(self, attributes=(), notattributes=(), attributes_file=os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'attributes.txt'))):
        self.attributes = attributes
        self.filenames = np.array([], dtype='str')
        self.attributes_file = attributes_file
        self.matches = 0

    def get_filenames(self, attributes=(), notattributes=()):
        with open(self.attributes_file, mode='rt') as file:
            next(file)
            possible_attributes = file.readline().strip()
        possible_attributes = possible_attributes.split(' ')
        # print(str(possible_attributes))

        if (attributes == () and self.attributes != ()):
            attributes = self.attributes
        attributes = tuple(map(lambda attribute: possible_attributes.index(
            attribute) if type(attribute) is str else attribute, attributes))
        attributes = (0,) + tuple(sorted([(attribute + 1)
                                          for attribute in attributes]))
        print(attributes)

        filenames = np.genfromtxt(self.attributes_file,
                                  dtype=str, skip_header=2, usecols=attributes)
        return np.array(list(map(lambda row: (row[0], (-1 if '-1' in row[1:] else 1)), filenames)), dtype=[('filename', 'U' + str(len(max(filenames[:, 0], key=len)))), ('label', '<i1')])

    def get_batch(self, no=64):
        return 0
