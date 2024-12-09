
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),

    path("mycandidates", views.candidates, name="candidates"),
    path("mycandidates/new", views.add_candidate, name="add_candidate"),
    path("mymandates", views.mandates, name="mandates"),

    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path('update-status/<int:candidate_id>/', views.update_status, name='update_status'),
    path('add-mandate/', views.add_mandate, name='add_mandate'),
]
