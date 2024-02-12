from django.urls import path
from . import views

urlpatterns = [
   path('',views.home,name="home"),
   path('/college_dashboard/',views.collegeLogin,name="collegeDashboard")
]
