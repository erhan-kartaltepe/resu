import json
import logging
import resu_const
import sys
from collections import namedtuple

# Convert a JSON string to object
def _json_object_hook(d): return namedtuple('X', d.keys())(*d.values())
def json2obj(data): return json.loads(data, object_hook=_json_object_hook)

class Driver:
    def main(self):
        print("Hello world")
        self._file = open("sample_data.json", "r")
        self.x = self._file.read()
        self.y = json2obj(self.x)
        print(self.y.modes.titles[0])

if __name__ == '__main__':
    try:
        Driver().main()
    except:
        e = sys.exc_info()[0]
        logging.basicConfig(format=resu_const.LOGGING_FORMAT)
        d = {'clientip': '192.168.0.1', 'user': 'erhank'}
        logger = logging.getLogger('resu')
        logger.error('Main: %s', 'Unable to construct main: %s' % e, extra=d)



# ID--name, city state, phone, kvps of headings based on type
# Summary--sentences.
# Experience--Company, city, state, from, to, title, list of stuff (sentence and type and sublist of skills)
# Technical Skills--list (name and type)
# Education--name, city, state, gpa, degree (BS, MS, Certification etc.), concentration
# Awards--sentence