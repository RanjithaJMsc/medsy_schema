from mongoengine import *
from datetime import datetime

from mongoengine import *
from datetime import datetime
from bson import ObjectId


class ActivityQuestion(EmbeddedDocument):

    question_id = ObjectIdField(default=ObjectId)  
    question = StringField(required=True)


class ActivityContent(Document):

    activity_id = ObjectIdField(required=True)

    paragraph = StringField()
    images = ListField(StringField())

    questions = EmbeddedDocumentListField(ActivityQuestion)

    created_at = DateTimeField(default=datetime.utcnow)
    updated_at = DateTimeField(default=datetime.utcnow)

    def save(self, *args, **kwargs):
        self.updated_at = datetime.utcnow()
        return super(ActivityContent, self).save(*args, **kwargs)

