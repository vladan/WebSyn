function(doc) {
  if(doc.doc_type == "Company" && doc.industries) {
    for(var i = 0; i < doc.industries.length; i++) {
      emit(doc.industries[i]);
    }
  }
}
