from django.db import models

from datetime import datetime

class Tracker(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    date_deleted = models.DateTimeField(null=True, blank=True)

    def delete(self):
        self.date_deleted = datetime.now()

    class Meta:
        abstract = True