from django.db import models

# Create your models here.

class SignupUser(models.Model):
    # Id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100)
    Username = models.CharField(max_length=20)
    Email = models.EmailField()
    Phone = models.IntegerField()
    Password = models.CharField(max_length=50)

    class Meta():
        db_table = 'User_Reg'

    def __str__(self):
        return self.Username


class AdDetails(models.Model):
    #Id = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=100)
    Email = models.EmailField()
    Contact = models.IntegerField()
    PostedBy = models.CharField(max_length=100)
    PostedOn = models.DateField()
    Description = models.CharField(max_length=200)
    Category = models.CharField(max_length=10)
    Location = models.CharField(max_length=100)
    IMG1 = models.ImageField(upload_to='media/')

    class Meta:
        db_table = 'Details'

    def __str__(self):
        return ( self.PostedBy )