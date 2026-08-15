from django.db import models

# Create your models here.


class Bride(models.Model):
  brideName = models.CharField(max_length=1000)
  brideDOB = models.DateField()
  brideEmail = models.EmailField(unique= True)
  brideFatherName =  models.CharField(max_length=1000)
  brideMotherName =  models.CharField(max_length=1000)
  brideAddress = models.CharField(max_length=1000)
  brideNidNo =  models.CharField(max_length=1000)
  brideImage=  models.ImageField(upload_to='documents/')
  brideNidImage =  models.ImageField(upload_to='documents/')
  is_valid = models.BooleanField(default=False)
  create_at = models.DateTimeField(auto_now_add=True)
  
  
  def __str__(self):
    return f"{self.brideName}"


class Groom(models.Model):
  groomName = models.CharField(max_length=1000)
  groomDOB = models.DateField()
  groomEmail = models.EmailField(unique= True)
  groomFatherName =  models.CharField(max_length=1000)
  groomMotherName =  models.CharField(max_length=1000)
  groomAddress = models.CharField(max_length=1000)
  groomNidNo =  models.CharField(max_length=1000)
  groomImage=  models.ImageField(upload_to='documents/')
  groomNidImage =  models.ImageField(upload_to='documents/')
  is_document_valid = models.BooleanField(default=False)
  create_at = models.DateTimeField(auto_now_add=True)

  
  def __str__(self):
    return f"{self.groomName}"
  
class MarrigaeRequest(models.Model):
     STATUS_CHOICES = [
        ('pending','Pending'),
        ('reject','Reject'),
        ('approve','Approve'),
      ]
     groom = models.ForeignKey(Groom,on_delete=models.CASCADE)
     bride =  models.ForeignKey(Bride,on_delete=models.CASCADE)
     status   =  models.CharField(max_length=1000,choices=STATUS_CHOICES,default='Pending')
     marriageDate = models.DateField()
     registrationDate = models.DateField()
     place_of_marriage = models.CharField(max_length=1000)
     
     def __str__(self):
       return f"{self.groom.groomName}&{self.bride.brideName}"
     
  
class MarriageRecorde(models.Model):
  marriageRequest = models.OneToOneField(MarrigaeRequest,on_delete=models.CASCADE)
  certificateNo = models.CharField(max_length=100)
  issuedDate = models.DateField(auto_now_add=True)
  
  
  
  def __str__(self):
    return self.certificateNo  


    
    
    
 