from django.urls import path, include
from .views import *

app_name = 'api'


urlpatterns = [
    path('courses/', CourseList.as_view(), name= 'course_list'),
    path('courses/<int:pk>/', CourseDetail.as_view(), name= 'course_detail'),

    path('terms/', TermList.as_view(), name= 'term_list'),
    path('terms/<int:pk>/', TermDetail.as_view(), name= 'term_detail'),

    path('professors/', ProfessorList.as_view(), name= 'professor_list'),
    path('professors/<int:pk>/', ProfessorDetail.as_view(), name= 'professor_detail'),

    path('students/', StudentList.as_view(), name= 'student_list'),
    path('students/<int:pk>/', StudentDetail.as_view(), name= 'student_detail'),

    path('managers/', ManagerList.as_view(), name= 'manager_list'),
    path('managers/<int:pk>/', ManagerDetail.as_view(), name= 'manager_detail'),

    path('presentations/', PresentationList.as_view(), name= 'presentation_list'),
    path('presentations/<int:pk>/', PresentationDetail.as_view(), name= 'presentation_detail'),

    path('gets/', GetList.as_view(), name= 'get_list'),
    path('gets/<int:pk>/', GetDetail.as_view(), name= 'get_detail'),

    path('users/', UserList.as_view(), name= 'user_list'),
    path('users/<int:pk>/', UserDetail.as_view(), name= 'user_detail'),
]