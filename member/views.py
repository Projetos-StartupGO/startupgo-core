from .models import (ServiceOffer, Member, Interest, Event, Company, Community,
                     Skill)
from .serializers import (ServiceOfferSerializer, MemberSerializer, InterestSerializer,
                          EventSerializer, CompanySerializer, CommunitySerializer,
                          SkillSerializer)
from rest_framework.viewsets import ModelViewSet


class MemberViewSet(ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer


class CommunityViewSet(ModelViewSet):
    queryset = Community.objects.all()
    serializer_class = CommunitySerializer


class CompanyViewSet(ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class EventViewSet(ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class ServiceOfferViewSet(ModelViewSet):
    queryset = ServiceOffer.objects.all()
    serializer_class = ServiceOfferSerializer


class InterestViewSet(ModelViewSet):
    queryset = Interest.objects.all()
    serializer_class = InterestSerializer


class SkillViewSet(ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

