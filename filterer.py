# Imports a list of attributes, returns the filenames that match (or doesn't match) the selected attributes.

import os
import numpy as np
from random import sample


class Filterer:
    def __init__(self, attributes=(), notattributes=(), attributes_file=os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'attributes.txt'))):
        self.attributes = attributes
        self.processed = None
        self.attributes_file = attributes_file
        self.matches = 0

    def get_filenames(self, attributes=(), notattributes=()):
        with open(self.attributes_file, mode='rt') as file:
            next(file)
            possible_attributes = file.readline().strip()
        possible_attributes = possible_attributes.split(' ')
        # print(str(possible_attributes))

        if (len(attributes) == 0 and len(self.attributes) != 0):
            attributes = self.attributes
        if (len(notattributes) == 0 and len(self.notattributes) != 0):
            notattributes = self.notattributes
        attributes, notattributes = tuple([tuple(attributeslist) if type(attributeslist) is not str else (
            attributeslist,) for attributeslist in (attributes, notattributes)])

        attributes, notattributes = (tuple(map(lambda attribute: possible_attributes.index(attribute) if type(
            attribute) is str else attribute, attributeslist)) for attributeslist in (attributes, notattributes))
        attributes, notattributes = tuple(tuple(sorted(tuple(
            (attribute + 1) for attribute in attributeslist))) for attributeslist in (attributes, notattributes))
        attributes = (0, *attributes)
        # print(attributes, notattributes)

        filenames = np.genfromtxt(self.attributes_file,
                                  dtype=str, skip_header=2, usecols=(attributes + notattributes))

        match = ['1' if attribute not in notattributes else '-1' for attribute in (
            attributes[1:] + notattributes)]

        # # Bonus generator vs list comprehension performance measurement:
        # from timeit import default_timer as timer
        # start = timer()
        # list(((row[0], 1 if np.array_equal(row[1:], match) else -1) for row in filenames))
        # t1 = timer() - start
        # [(row[0], 1 if np.array_equal(row[1:], match) else -1) for row in filenames] # Faster
        # t2 = timer() - t2
        # print(t1, t2)
        processed = np.array([(row[0], 1 if np.array_equal(row[1:], match) else -1) for row in filenames], dtype=[('filename', 'U' + str(len(max(filenames[:, 0], key=len)))), ('label', '<i1')])
        self.processed = processed
        return processed

    def get_batch(self, no=64):
        return sample(self.processed, no)
