from django.urls import path
from . import views

urlpatterns=[
    path('/parts',views.part_index.as_view(),name='part_index'),
    path('/<str:part_name>',views.show_part.as_view(),name='show_part'),
    path('/<str:part>/<int:wid>',views.show_exercise.as_view(),name='show_exercise'), 
    ]