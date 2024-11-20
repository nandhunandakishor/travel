from django.db import models

# Create your models here.

class blog(models.Model):
    Username=models.CharField(max_length=100)
    Password=models.CharField(max_length=100)

class user(models.Model):
      LOGIN=models.ForeignKey(blog,on_delete=models.CASCADE)
      Username=models.CharField(max_length=20)
      Email=models.CharField(max_length=50)

def __str__(self):
        return self.Name

class BachelorPackage(models.Model):
    Fullname = models.CharField(max_length=100)
    Email = models.EmailField(max_length=100)
    Phonenumber = models.IntegerField()
    Checkin = models.DateField()
    Checkout = models.DateField()
    Roomtype = models.CharField(max_length=100)
    Numberofguest = models.IntegerField()
    Specialrequest = models.CharField(max_length=200, blank=True, null=True)  # Optional field

    def __str__(self):
        return self.Fullname


class calicutbook(models.Model):
     cFullname = models.CharField(max_length=100)
     cEmail = models.EmailField(max_length=100)
     cPhonenumber = models.IntegerField()
     cTripdate = models.DateTimeField()
     cTravelers = models.IntegerField()
     cSpecialrequest = models.CharField(max_length=200, blank=True, null=True)

     def __str__(self):
          return self.cFullname
