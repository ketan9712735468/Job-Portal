from django import views
from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from django.conf import settings

urlpatterns = [
    path('register/',views.registe_view,name="register"),
    path('login/',views.login_view,name="login"),
    path('',views.home,name="home"),
    path('job/',views.job_view,name="job"),
    path('logout/', LogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),
]