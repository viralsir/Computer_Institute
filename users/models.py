from django.db import models
from django.contrib.auth.models import User
#from PIL import Image


# Create your models here.
# class profile(models.Model):
#     user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
#     image = models.ImageField(default='default.jpg',upload_to='profile_pics')
#
#
#     def __str__(self):
#         return f"{self.user.username} profile"
#
#     def save(self,*args,**kwargs):
#         super().save(*args,**kwargs)
#         img=Image.open(self.image.path)
#
#         if img.width>300 or img.height>300:
#             outputsize=(300,300)
#             img.thumbnail(outputsize)
#             img.save(self.image.path)
#
#         # adding date calender in createview plase put this code in createview
#         # from django.forms.extras.widgets import SelectDateWidget
#         # form = super(EnvironmentCreateView, self).get_form()
#         # form.fields['creation_date'].widget = SelectDateWidget()
#         # return form