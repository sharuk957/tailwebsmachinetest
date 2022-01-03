from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
from django.urls.conf import include


router = DefaultRouter()
router.register('subject',views.SubjectView,basename="subject")
router.register('',views.StudentView,basename="students")


urlpatterns = [
    path('',include(router.urls)),
]
