from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Student, Subject


class SubjectSerializer(ModelSerializer):
    class Meta:
        model  = Subject
        fields = "__all__"


class StudentSerializer(ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"