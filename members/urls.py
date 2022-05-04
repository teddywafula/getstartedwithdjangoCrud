from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:member_id>/show/', views.show, name='show'),
    path('store/', views.store, name='store'),
    path('<int:member_id>/edit/', views.edit, name='edit'),
    path('update/<int:member_id>', views.update, name='update'),
    path('<int:member_id>/delete/', views.delete, name='delete'),
]