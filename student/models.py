from django.db import models
from django.urls import reverse


class Student(models.Model):
    class Gender(models.IntegerChoices):
        MALE = 1
        FEMALE = 2
    family_name = models.CharField(max_length=20)
    given_name = models.CharField(max_length=20)
    family_name_huri = models.CharField(max_length=50)
    given_name_huri = models.CharField(max_length=50)
    birth = models.CharField(max_length=10)
    gender = models.IntegerField(choices=Gender.choices)
    address = models.CharField(max_length=50)
    career = models.TextField(blank=True)
    firstyear_class = models.IntegerField(null=True, blank=True)
    firstyear_number = models.IntegerField(null=True, blank=True)
    secondyear_class = models.IntegerField(null=True, blank=True)
    secondyear_number = models.IntegerField(null=True, blank=True)
    thirdyear_class = models.IntegerField(null=True, blank=True)
    thirdyear_number = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.family_name + self.given_name + " (" + self.birth + ")"

    def get_absolute_url(self):
        return reverse('detail', args=[str(self.id)])


class Parent(models.Model):
    student = models.ForeignKey(Student, on_delete= models.CASCADE)
    parent_family_name = models.CharField(max_length=20)
    parent_given_name = models.CharField(max_length=20, default=None, null=True)
    parent_family_name_huri = models.CharField(max_length=20, default=None, null=True)
    parent_given_name_huri = models.CharField(max_length=20, default=None, null=True)

    def __str__(self):
        return "保護者名：" + self.parent_family_name + self.parent_given_name


class SchoolIn(models.Model):
    name = models.ForeignKey(Student, on_delete=models.CASCADE)
    date_entrance = models.DateField()
    grade_entrance = models.IntegerField()
    before_entrance = models.CharField(max_length=50)


class SchoolOut(models.Model):
    name = models.ForeignKey(Student, on_delete=models.CASCADE)
    date_out = models.DateField()
    after_out = models.CharField(max_length=50)


class Graduation(models.Model):
    name = models.ForeignKey(Student, on_delete=models.CASCADE)
    date_graduation = models.DateField()
    after_graduation = models.CharField(max_length=100)
