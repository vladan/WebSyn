from blueprints.couchforum import couch_forum
from blueprints.staticpages import static_page

# this has got to be be rewritten
blueprint_list = [couch_forum, (static_page, "/p")]
