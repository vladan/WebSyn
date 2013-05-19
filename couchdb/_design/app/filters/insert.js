function(doc) {
  if (doc.doc_type == 'Post' && doc._rev.indexOf("1-") == 0) {
    return true;
  }
  else {
    return false;
  }
}
