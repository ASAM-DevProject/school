from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import *
from collection.models import *
from django.contrib.auth.models import User
from rest_framework.permissions import IsAdminUser
# Create your views here.

class CourseList(ListCreateAPIView):
    queryset = CourseModel.objects.all()
    serializer_class = CourseSerializer
    filterset_fields = ['unit']
    search_fields = ['name']
    ordering_fields = ['date']

class CourseDetail(RetrieveUpdateDestroyAPIView):
    queryset = CourseModel.objects.all()
    serializer_class = CourseSerializer


class TermList(ListCreateAPIView):
    queryset = TermModel.objects.all()
    serializer_class = TermSerializer
    filterset_fields = ['name']
    search_fields = ['name']
    ordering_fields = ['date']

class TermDetail(RetrieveUpdateDestroyAPIView):
    queryset = TermModel.objects.all()
    serializer_class = TermSerializer

class ProfessorList(ListCreateAPIView):
    queryset = ProfessorModel.objects.all()
    serializer_class = ProfessorSerializer
    filterset_fields = ['status', 'user']
    search_fields = ['user', 'status']
    ordering_fields = ['date']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ProfessorDetail(RetrieveUpdateDestroyAPIView):
    queryset = ProfessorModel.objects.all()
    serializer_class = ProfessorSerializer

class StudentList(ListCreateAPIView):
    queryset = StudentModel.objects.all()
    serializer_class = StudentSerializer
    filterset_fields = ['status', 'user']
    search_fields = ['status', 'user']
    ordering_fields = ['date']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class StudentDetail(RetrieveUpdateDestroyAPIView):
    queryset = StudentModel.objects.all()
    serializer_class = StudentSerializer

class ManagerList(ListCreateAPIView):
    queryset = ManagerModel.objects.all()
    serializer_class = ManagerSerializer
    filterset_fields = ['status', 'user']
    search_fields = ['status', 'user']
    ordering_fields = ['date']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ManagerDetail(RetrieveUpdateDestroyAPIView):
    queryset = ManagerModel.objects.all()
    serializer_class = ManagerSerializer

class PresentationList(ListCreateAPIView):
    queryset = PresentationModel.objects.all()
    serializer_class = PersentationSerializer
    filterset_fields = ['status', 'user']
    search_fields = ['status', 'user']
    ordering_fields = ['date']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        serializer.save(term=self.term)
        serializer.save(course=self.course)


class PresentationDetail(RetrieveUpdateDestroyAPIView):
    queryset = PresentationModel.objects.all()
    serializer_class = PersentationSerializer

class GetList(ListCreateAPIView):
    queryset = GetModel.objects.all()
    serializer_class = GetSerializer
    filterset_fields = ['status', 'get']
    search_fields = ['get']
    ordering_fields = ['date']

class GetDetail(RetrieveUpdateDestroyAPIView):
    queryset = GetModel.objects.all()
    serializer_class = GetSerializer

class UserList(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser,)
    filterset_fields = ['is_staff', 'is_superuser', 'username']
    search_fields = ['username', 'email']
    ordering_fields = ['date_joined', 'last_login', 'id']


class UserDetail(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser,)