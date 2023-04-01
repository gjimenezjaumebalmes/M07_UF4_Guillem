from django.urls import path
from .views import homePageView
from . import views
from .views import ProfesorDetailView
from .views import AlumnoDetailView

urlpatterns = [
    path("", homePageView, name="home"),
    path('profesorado/', views.profesorado, name='profesor_list'),
    path('alumnado/', views.alumnado, name='alumno_list'),
    path('profesorado/<int:pk>/', ProfesorDetailView.as_view(), name='profesor_detail'),
    path('alumnado/<int:pk>/', AlumnoDetailView.as_view(), name='alumno_detail'),
]

