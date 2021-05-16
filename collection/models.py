from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
# Create your models here.

class CourseModel(models.Model):
    name = models.CharField(max_length=100)
    unit = models.IntegerField(default=1)
    date = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class TermModel(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class ProfessorModel(models.Model):
    user = models.ForeignKey(to = get_user_model(), on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)


class StudentModel(models.Model):
    user = models.ForeignKey(to = get_user_model(), on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)


class ManagerModel(models.Model):
    user = models.ForeignKey(to = get_user_model(), on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)


class PresentationModel(models.Model):
    user = models.ForeignKey(to = get_user_model(), on_delete=models.CASCADE)
    course = models.ForeignKey(to = CourseModel, on_delete=models.CASCADE)
    term = models.ForeignKey(to = TermModel, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)


class GetModel(models.Model):
    presentation = models.ForeignKey(to = PresentationModel, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)