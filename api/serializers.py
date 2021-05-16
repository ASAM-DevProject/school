from rest_framework import serializers
from collection.models import *
from django.contrib.auth import get_user_model
from drf_dynamic_fields import DynamicFieldsMixin


class CourseSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = CourseModel
        fields = '__all__'

    # for test validate at django_rest_framework
    # def validate_name(self, value):
    #     filter_list = ['javascript', 'laravel', 'PHP']
    #     for i in filter_list:
    #         if i in value:
    #             raise serializers.ValidationError(f"don't use bad word : {i}")

class TermSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = TermModel
        fields = '__all__'

class ProfessorSerializer(DynamicFieldsMixin, serializers.ModelSerializer):

    def get_user(self, obj):
        return {
            "username": obj.user.username,
            "first_name": obj.user.first_name,
            "last_name": obj.user.last_name
        }

    user = serializers.SerializerMethodField('get_user')
    class Meta:
        model = ProfessorModel
        fields = '__all__'

class StudentSerializer(DynamicFieldsMixin, serializers.ModelSerializer):

    def get_user(self, obj):
        return {
            "username" : obj.user.username,
            "first_name" : obj.user.first_name,
            "last_name" : obj.user.last_name
        }

    user = serializers.SerializerMethodField('get_user')
    class Meta:
        model = StudentModel
        fields = '__all__'

class ManagerSerializer(DynamicFieldsMixin, serializers.ModelSerializer):

    def get_user(self, obj):
        return {
            "username": obj.user.username,
            "first_name": obj.user.first_name,
            "last_name": obj.user.last_name
        }

    user = serializers.SerializerMethodField('get_user')
    class Meta:
        model = ManagerModel
        fields = '__all__'

class PersentationSerializer(DynamicFieldsMixin, serializers.ModelSerializer):

    class Meta:
        model = PresentationModel
        fields = ['user', 'course', 'term', 'date', 'status']


    user = serializers.SerializerMethodField()
    course = serializers.SerializerMethodField()
    term = serializers.SerializerMethodField()

    def get_user(self, obj):
        return {
            "username": obj.user.username,
            "first_name": obj.user.first_name,
            "last_name": obj.user.last_name
        }

    def get_course(self, obj):
        return {
            "name": obj.course.name,
            "unit": obj.course.unit
        }

    def get_term(self, obj):
        return {
            "name": obj.term.name
        }


class GetSerializer(DynamicFieldsMixin, serializers.ModelSerializer):

    class Meta:
        model = GetModel
        fields = '__all__'

class UserSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = '__all__'