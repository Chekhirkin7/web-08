from mongoengine import connect, StringField, Document, BooleanField

connect(db='homework_08',
        host='mongodb+srv://user_hw_08:567234@cluster0.p4i2j.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')

class Contact(Document):
    fullname = StringField(required=True)
    email = StringField(required=True, unique=True)
    message_sent = BooleanField(default=False)

    meta = {'collection': 'contacts'}