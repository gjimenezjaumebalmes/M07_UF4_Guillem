from django.urls import path
from .views import homePageView
from . import views
from .views import ProfesorDetailView

urlpatterns = [
    path("", homePageView, name="home"),
    path('profesorado/', views.profesorado, name='profesorado_list'),
    path('alumnado/', views.alumnado, name='alumnado'),
    path('profesorado/<int:pk>/', ProfesorDetailView.as_view(), name='profesorado_detail'),
]