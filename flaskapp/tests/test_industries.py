import unittest
from couchdbkit import (Document, StringProperty, ListProperty,
        DateTimeProperty, SchemaProperty, IntegerProperty)

from blueprints.couchforum.models import Company



class TestCouchFilters(unittest.TestCase):
    """
    Test case for the filters on the CouchDB Changes API
    """
    @clasmethod
    def setUpClass(cls):
        companies = []
        companies.push(Company.wrap('{"industries": ["Banking"], "name": "Komercijalna", "url": "kb.com.mk", "address": "komercijalna ds"}'))
        companies.push(Company.wrap('{"industries": ["IT", "Software"], "name": "Seavus", "url": "seavus.com.mk", "address": "seavus ds"}'))
        companies.push(Company.wrap('{"industries": ["IT", "Software"], "name": "ITGma", "url": "itgma.com.mk", "address": "itgma ds"}'))
        companies.push(Company.wrap('{"industries": ["Banking"], "name": "NLB", "url": "nlb.com.mk", "address": "nlb ds"}'))
        companies.push(Company.wrap('{"industries": ["Banking"], "name": "Komercijalna", "url": "kb.com.mk", "address": "ds"}'))


    def setUp(self):
        # should initialize a change subscriber that will
        # fill a list with the values that it receives
        pass
