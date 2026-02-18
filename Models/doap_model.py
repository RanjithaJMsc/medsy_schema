from mongoengine import *
from datetime import datetime
from Models.admin_model import Admin
from Models.course_model import Course
from Models.year_model import Year
from Models.subject_model import Subject
from Models.layer1_model import Layer_1
from Models.layer2_model import Layer_2


class ActivityRef(EmbeddedDocument):
    activity_id = ObjectIdField(required=True)
    activity_name = StringField(required=True)
    activity_type = StringField(
        choices=["OSPE","OSCE","INTERPRETATION","IMAGE"],
        required=True
    )


class Doap(Document):

    course = ReferenceField(Course)
    year = ReferenceField(Year)
    subject = ReferenceField(Subject)
    layer1 = ReferenceField(Layer_1)
    layer2 = ReferenceField(Layer_2)

    activities = EmbeddedDocumentListField(ActivityRef)

    created_by = ReferenceField(Admin)

    created_at = DateTimeField(default=datetime.utcnow)
    updated_at = DateTimeField(default=datetime.utcnow)
