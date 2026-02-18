from mongoengine import *
from datetime import datetime
from Models.doap_model import Doap
from Models.user_model import User
from Models.admin_model import Admin


class DoapAssignment(Document):

    doap = ReferenceField(Doap, required=True)   

    activity_id = ObjectIdField(required=True)  

    assigned_to = ListField(ReferenceField(User)) 
    assigned_by = ReferenceField(Admin)            

    assigned_at = DateTimeField(default=datetime.utcnow)
    updated_at = DateTimeField(default=datetime.utcnow)

    def save(self, *args, **kwargs):
        self.updated_at = datetime.utcnow()
        return super(DoapAssignment, self).save(*args, **kwargs)
