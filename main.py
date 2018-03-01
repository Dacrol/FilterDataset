# Imports a list of attributes, returns the filenames that match (or doesn't match) the selected attributes.

import os
import numpy as np


class Filterer:
    def __init__(self, attributes=(0), attributes_file='attributes.txt'):
        self.attributes = attributes
        self.filenames = np.array()
        self.attributes_file = attributes_file
        self.matches = 0

    def get_filenames(self):
        filenames = np.loadtxt(self.attributes_file,
                               dtype=str, skiprows=1, usecols=self.attributes)
        return filenames

    def get_batch(self, no=64):
        return 0
