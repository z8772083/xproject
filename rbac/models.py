from django.db import models

class User(models.Model):

    gender_choice=(
        (0,'男'),
        (1,'女')
    )

    name = models.CharField(max_length=30,unique=True,verbose_name='姓名')

    age = models.IntegerField(verbose_name='年龄')

    gender = models.IntegerField(choices=gender_choice,verbose_name='性别')

    telephone = models.IntegerField(verbose_name='电话')

    role=models.ForeignKey(to='Role',on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Role(models.Model):

    title = models.CharField(max_length=30,verbose_name='角色')

    def __str__(self):
        return self.title