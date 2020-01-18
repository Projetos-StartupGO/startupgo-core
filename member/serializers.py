from .models import (Member, Community, Company, Event, Skill, Interest,
                     ServiceOffer)

from rest_framework import serializers


class SkillSerializer(serializers.ModelSerializer):

    class Meta:
        model = Skill
        fields = ['id', 'name']


class MemberSerializer(serializers.ModelSerializer):

    skill = SkillSerializer(many=True, required=True)

    class Meta:
        model = Member
        fields = ['first_name', 'last_name', 'email', 'is_superuser', 'is_admin',
                  'created', 'modified', 'skill']


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
