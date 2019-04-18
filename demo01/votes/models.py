from django.db import models

# Create your models here.


class Questions(models.Model):
    qcontain = models.CharField(max_length=100)

    def __str__(self):
        return self.qcontain


class Choices(models.Model):
    cchoose = models.CharField(max_length=20)
    ccount = models.IntegerField(default=0)
    cvalues = models.ForeignKey('Questions', on_delete=models.CASCADE)


