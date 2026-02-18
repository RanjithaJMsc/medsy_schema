from mongoengine import *
from datetime import datetime
from Models.doap_model import Doap
from Models.user_model import User


class Answer(EmbeddedDocument):

    question_id = ObjectIdField(required=True)
    answer_text = StringField()


class StudentSubmission(Document):

    student = ReferenceField(User, required=True)

    doap = ReferenceField(Doap, required=True)
    activity_id = ObjectIdField(required=True)  

    started = BooleanField(default=False)
    completed = BooleanField(default=False)

    answers = EmbeddedDocumentListField(Answer)

    created_at = DateTimeField(default=datetime.utcnow)
    updated_at = DateTimeField(default=datetime.utcnow)

    def save(self, *args, **kwargs):
        self.updated_at = datetime.utcnow()
        return super(StudentSubmission, self).save(*args, **kwargs)
