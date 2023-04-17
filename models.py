from mongoengine import (Document, DateTimeField, DictField, StringField, IntField, BooleanField, UUIDField,
                         URLField, ListField, EmbeddedDocument, EmbeddedDocumentField)

class Article(Document):
    id = UUIDField(primary_key=True)
    title = StringField()
    pubdate = DateTimeField()
    content = StringField()
