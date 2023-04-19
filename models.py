from mongoengine import (Document, DateTimeField, DictField, StringField, IntField, BooleanField, UUIDField,
                         URLField, ListField, EmbeddedDocument, EmbeddedDocumentField)

class Article(Document):
    article_no = IntField()
    title = StringField()
    pub_date = DateTimeField()
    content = StringField()


class Writings(Document):
    article_no = IntField()
    title = StringField()
    pub_date = DateTimeField()
    content = StringField()