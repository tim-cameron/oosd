__author__ = 'camertp1'


import covert_factory

class OriginalDocument:

    orig = { 'name': 'Tom',
             'role': 'Lecturer',
             'hobbies': ['scuba', 'taekwondo', 'beekeeping'],
             'favourite_beer': {'brewer': 'Rodenbach',
                                'beer': 'Grand Cro'}
    }

    def __init__(self):
        self.factory = covert_factory.ConvertFactory(self.orig)
