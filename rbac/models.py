from django.db import models

class User(models.Model):

    gender_choice=(
        (0,'男'),
        (1,'女')
    )
    project_choice=(
        ('g','G项目'),
        ('l','L项目'),
        ('r','R项目')
    )

    name = models.CharField(max_length=30,unique=True,verbose_name='姓名')

    age = models.IntegerField(verbose_name='年龄')

    gender = models.IntegerField(choices=gender_choice,verbose_name='性别')

    telephone = models.IntegerField(verbose_name='电话')

    role=models.ForeignKey(to='Role',on_delete=models.CASCADE)

    project = models.CharField(choices=project_choice,max_length=20,verbose_name='项目')

    def __str__(self):
        return self.name

class Role(models.Model):

    title = models.CharField(max_length=30,verbose_name='角色')

    def __str__(self):
        return self.title


class CR(models.Model):

    user = models.CharField(max_length=20)
    channel = models.CharField(max_length=30)
