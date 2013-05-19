function(doc) {
    if(doc.doc_type == "Company") {
        emit(doc._id, doc)
    }
}
