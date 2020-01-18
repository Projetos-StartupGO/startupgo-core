from django.urls import path, include

from rest_framework import routers

from .views import (CompanyViewSet, EventViewSet, CommunityViewSet, InterestViewSet,
                    MemberViewSet, SkillViewSet, ServiceOfferViewSet)


router = routers.DefaultRouter()
router.register('member', MemberViewSet)
router.register('community', CommunityViewSet)
router.register('company', CompanyViewSet)
router.register('event', EventViewSet)
router.register('interest', InterestViewSet)
router.register('skill', SkillViewSet)
router.register('service-offer', ServiceOfferViewSet)

urlpatterns = (
    # urls for Django Rest Framework API
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls')),
)
