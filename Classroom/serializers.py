from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from django.contrib.auth.models import User
from .models import *
from builtins import object


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username',)


class UserSerializerWithToken(serializers.ModelSerializer):

    token = serializers.SerializerMethodField()
    password = serializers.CharField(write_only=True)

    def get_token(self, obj):
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(obj)
        token = jwt_encode_handler(payload)
        return token

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    class Meta:
        model = User
        fields = ('token', 'username',)
        
        
        
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('__all__')


class ProfessorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Professor
        fields = ('__all__',)


class SectionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Section
        fields = ('__all__',)


class ClassMeetingSerializer (serializers.ModelSerializer):
    class Meta:
        model = ClassMeeting
        fields = ('__all__',)


class NoteSerializer (serializers.ModelSerializer):
    class Meta:
        model = Note
        fields =('__all__',)


class CommentSerializer (serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('__all__',)


class EventSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Event
        fields = ('__all__',)


class ReviewSerializer(object):
    def __init__(self, body):
        self.body = body

    @property
    def all_reviews(self):
        output = {'reviews': []}

        for review in self.body:
            review_detail = {
                'student': review.User.username,
                'section': review.class_section.section_title,
                'description': review.description,
                'Professor': review.Professor.last_name

            }
            output['reviews'].append(review_detail)

        return output

    @property
    def review_detail(self):
        output = {'review': []}

        for review in self.body:
                review_detail = {
                'student': review.User,
                'section': review.class_section,
                'description': review.description,
                'Professor': review.Professor.last_name
            }
                output['review'].append(review_detail)

        return output
        
        
class AlertSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Alert
        fields =('__all__',)
    
