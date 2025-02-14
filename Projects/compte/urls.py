from django.urls import path
from . import views

urlpatterns = [
    path('connection/', views.connection,name="connection"),
    path('inscription/', views.inscription, name="inscription"),
    path("admins/", views.admin, name="admin"),
    path('cours/<str:slug>/',views.cours,name="cours")
]
 