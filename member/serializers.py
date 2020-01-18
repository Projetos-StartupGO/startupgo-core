from .models import (Member, Community, Company, Event, Skill, Interest,
                     ServiceOffer)

from rest_framework import serializers


class SkillSerializer(serializers.ModelSerializer):

    class Meta:
        model = Skill
        fields = '__all__'


class MemberSerializer(serializers.ModelSerializer):

    skill = SkillSerializer()

    class Meta:
        model = Member
        exclude = ['password', 'is_superuser', 'is_staff', 'is_active', 'date_joined',
                   'created', 'modified', 'groups', 'user_permissions', 'username']


class CommunitySerializer(serializers.ModelSerializer):

    class Meta:
        model = Community
        fields = '__all__'


class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = '__all__'


class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Event
        fields = '__all__'


class InterestSerializer(serializers.ModelSerializer):

    class Meta:
        model = Interest
        fields = '__all__'


class ServiceOfferSerializer(serializers.ModelSerializer):

    class Meta:
        model = ServiceOffer
        fields = '__all__'
