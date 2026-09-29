from django.urls import path

from . import views


urlpatterns = [

    path(
        '',
        views.index,
        name='home'
    ),

    path(
        'add/',
        views.add_member,
        name='add_member'
    ),

    path(
        'edit/<int:id>/',
        views.edit_member,
        name='edit_member'
    ),

    path(
        'delete/<int:id>/',
        views.delete_member,
        name='delete_member'
    ),
    path(
    'workout/add/',
    views.add_workout,
    name='add_workout'
),
path(
    'member/<int:member_id>/workout/add/',
    views.add_workout,
    name='add_workout'
),
]