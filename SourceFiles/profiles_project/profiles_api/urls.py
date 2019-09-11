from django.conf.urls import url
from django.conf.urls import include

from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSets, base_name='hello-viewset')
router.register('profile', views.UserProfileViewSet)
router.register('login', views.LoginViewSet, base_name='login-viewset')
router.register('feed', views.UserProfileFeedViewSet)
# this file basically maps a certain keyword in the url to a certain APIView
urlpatterns = [
    url(r'^hello-view/', views.HelloAPIView.as_view()),
    url(r'', include(router.urls))
]
