from django.urls import path
from . import views
from .utils import loginValidation

#Create your urls here
urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    path('login/', views.signin, name="login"),
    path('login-process/', loginValidation.loginProcess, name="login-process"),
    path('logout/', views.signout, name="logout"),
    path('tesis_detail/<int:tesis_id>/', views.tesis_detail, name="tesis_detail"),
    path('tesis_detail/<int:tesis_id>/descargar/', views.descargar_tesis, name="descargar_tesis"),
    path('cargar_tesis/', views.cargar_tesis, name="cargar_tesis"),
    path('categorias/', views.categorias, name="categorias"),
]
