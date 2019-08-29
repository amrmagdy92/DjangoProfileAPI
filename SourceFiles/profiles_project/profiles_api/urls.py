from django.conf.urls import url
from . import views

# this file basically maps a certain keyword in the url to a certain APIView
urlpatterns = [
    url(r'^hello-view/', views.HelloAPIView.as_view()),
]
