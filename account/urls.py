from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
from django.urls.conf import include


router = DefaultRouter()
router.register('registration',views.RegistrationView,basename="registration")

urlpatterns = [
    path('api/',include(router.urls)),
    path('',views.LoginView.as_view(),name="login")

]
