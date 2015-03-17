__author__ = 'camertp1'
import yaml

class YAMLDocument:

    def __init__(self, og_data):
        self.og_data = og_data

    def convert(self):
        ret = yaml.dump(self.og_data)

        return ret