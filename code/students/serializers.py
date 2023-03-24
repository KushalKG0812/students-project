from rest_framework import serializers
from .models import *


class SubjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Subjects
        fields = '__all__'


class TeacherSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Teachers
        fields = '__all__'
