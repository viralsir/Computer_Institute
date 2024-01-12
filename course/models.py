from django.core.validators import MinValueValidator
from django.db import models
from django.urls import reverse

# Create your models here.
class course(models.Model):
    name=models.CharField(max_length=55)
    overview=models.TextField(blank=True,editable=True,null=True,verbose_name="Overview of Course :")
    description=models.TextField(blank=True,null=True)
    durations=models.IntegerField(validators=[MinValueValidator(0,"Durations should not be nagetive")],blank=True,null=True)
    fees=models.IntegerField(validators=[MinValueValidator(0,"Fees should not be Nagetive")])
    status=models.CharField(max_length=55,choices=[('Active','Active'),('Deactive','Deactive'),('Pending','Pending')])
    #user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='courses',null=True,blank=True)

    def __str__(self):
        return f" {self.name} "

    def get_absolute_url(self):
        return reverse('course-view')
