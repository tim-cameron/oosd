__author__ = 'camertp1'

import to_xml
import to_yaml
import to_json

class ConvertFactory:

    def __init__(self, data):
        self.data = data
        
    def converter(self, to_type):
        if (to_type == 'xml'):
            return to_xml.XMLDocument(self.data)
        elif(to_type == 'yaml'):
            return to_yaml.YAMLDocument(self.data)
        elif(to_type == 'json'):
            return to_json.JSONDocument(self.data)
        else:
            return None

