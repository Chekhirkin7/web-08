from tkinter.constants import CASCADE

from mongoengine import connect, Document, StringField, ListField, ReferenceField

connect(db='homework_08',
        host='mongodb+srv://user_hw_08:567234@cluster0.p4i2j.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')


class Author(Document):
    fullname = StringField(required=True, unique=True)
    born_date = StringField(max_length=50)
    born_location = StringField(max_length=150)
    description = StringField()
    meta = {'collection': 'authors'}

class Quote(Document):
    tags = ListField(StringField(max_length=15))
    author = ReferenceField(Author, reverse_delete_rule=CASCADE)
    quote = StringField()
    meta = {'collection': 'qoutes'}