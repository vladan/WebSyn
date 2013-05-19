from couchdbkit import Document, DocumentBase, SchemaProperty, StringProperty,\
    DateTimeProperty, IntegerProperty, ListProperty
import simplejson
import datetime


class Company(Document):
    """
    Class for company objects.
    Each company has default type set to "company"
    """
    name = StringProperty()
    address = StringProperty()
    industries = ListProperty()
    url = StringProperty()
    created_on = DateTimeProperty(default=datetime.datetime.now())


class Topic(Document):
    company = SchemaProperty(Company())
    title = StringProperty()
    created_on = DateTimeProperty(default=datetime.datetime.now())


class Post(Document):
    topic = SchemaProperty(Topic())
    upvotes = IntegerProperty(default=0)
    downvotes = IntegerProperty(default=0)
    content = StringProperty()
    created_on = DateTimeProperty(default=datetime.datetime.now())
