from django.db import models
import uuid


class Subjects(models.Model):
    sub_code = models.CharField(null=False, primary_key=True, max_length=100)
    sub_name = models.CharField(null=False, max_length=100)
    sub_abbreviation = models.CharField(null=False, max_length=100)
    sub_type = models.CharField(null=False, max_length=100)
    teacher_name = models.CharField(null=False, max_length=100)

    class Meta:
        verbose_name = "Subject"


class Teachers(models.Model):
    id = models.UUIDField(null=False, primary_key=True, default=uuid.uuid4)
    name = models.CharField(null=False, max_length=200)

    class Meta:
        verbose_name = "Teacher"
