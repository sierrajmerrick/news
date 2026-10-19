from django.urls import path
from .views import SignUpView, home_view, ta_detail_view, add_hours_view

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("", home_view, name = "home"),
    path("ta/<int:pk>/", ta_detail_view, name="ta_detail"),
    path("add-hours/", add_hours_view, name="add_hours"),
]