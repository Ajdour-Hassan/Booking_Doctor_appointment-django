from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.signals import post_save
from django.utils.text import slugify

#create dic choice !

type_of_person = (
  ('M' , "Male"),
  ('F' , "Female"),
)

# Create your models here.
class Profile(models.Model):
    Doctor_in = {
      ('a', 'Dentist'),
      ('a', 'eyes Doctor'),
      ('a', 'Physiologist'),
      ('a', 'psychologist'),
    }
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=15 , default="")
    gender = models.CharField(max_length=30, choices=type_of_person)
    specialist = models.CharField(max_length=30 , default="")
    field = models.CharField(max_length=30 , choices=Doctor_in , blank=True, null=True)
    about = models.TextField(max_length=300 , default="")
    price = models.IntegerField(default=100)
    address = models.CharField(blank=True , null=True , max_length=40 )
    city = models.CharField(max_length=15 , default="")
    phon = models.CharField(default="+2126" , max_length=13)
    email= models.CharField(max_length=20, blank = True , null=True)
    facebook = models.CharField(max_length=20, blank=True , null=True)
    whatssap = models.CharField(default="+2126" , max_length=13 , blank=True , null = True)
    profile_joined = models.DateTimeField(default=timezone.now)
    joined = models.DateTimeField(auto_now=True)
    image = models.ImageField(default='doc.jpg', upload_to="./images")
    slug = models.SlugField(blank=True, null=True)

    def __str__(self):
      return 'User : ' + self.username

    class Meta():
      ordering = ('-price',)


    def save(self, *arg , **kwargs):
      if not self.slug:
       self.slug = slugify(self.username)
       super(Profile , self).save(*arg , **kwargs)


def create_profile(sender , **kwargs):
  if kwargs['created']:
    Profile.objects.create(user=kwargs['instance'])
post_save.connect(create_profile , sender=User)



