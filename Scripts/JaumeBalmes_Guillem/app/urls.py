from django.urls import path
from .views import homePageView, profesorado, alumnado, ProfesorDetailView, AlumnoDetailView, ProfesorDeleteView, AlumnoDeleteView, profesor_edit, alumno_edit

urlpatterns = [
    path("", homePageView, name="home"),
    path('profesorado/', profesorado, name='profesor_list'),
    path('alumnado/', alumnado, name='alumno_list'),
    path('profesorado/<int:pk>/', ProfesorDetailView.as_view(), name='profesor_detail'),
    path('alumnado/<int:pk>/', AlumnoDetailView.as_view(), name='alumno_detail'),
    path('profesor-delete/<int:pk>/', ProfesorDeleteView.as_view(), name='profesor_delete'),
    path('alumno-delete/<int:pk>/', AlumnoDeleteView.as_view(), name='alumno_delete'),
    path('profesor-edit/<int:pk>/', profesor_edit, name='profesor_edit'),
    path('alumno-edit/<int:pk>/', alumno_edit, name='alumno_edit'),
]