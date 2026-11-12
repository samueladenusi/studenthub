
from django.urls import path
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView
from . import views

urlpatterns = [

    # Root URL: Redirect to dashboard
    path(
        '',
        RedirectView.as_view(
            pattern_name='dashboard',
            permanent=False
        ),
        name='home'
    ),

    # Authentication URLs
    path(
        'login/',
        auth_views.LoginView.as_view(
            template_name='login.html',
            redirect_authenticated_user=True
        ),
        name='login'
    ),

    path(
        'logout/',
        auth_views.LogoutView.as_view(next_page='login'),
        name='logout'
    ),

    # Dashboard
    path('dashboard/', views.dashboard, name='dashboard'),

    # Student Management URLs
    path('add-student/', views.add_student, name='add_student'),

    path('students/', views.student_list, name='student_list'),

    path(
        'students/<int:student_id>/',
        views.student_detail,
        name='student_detail'
    ),

    path(
        'students/<int:student_id>/edit/',
        views.edit_student,
        name='edit_student'
    ),
]
