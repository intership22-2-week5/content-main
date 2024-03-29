from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.core.validators import RegexValidator

"""
class User(AbstractBaseUser):
    email = models.EmailField(
      'email address',
      unique=True, 
      error_messages={
        'unique': 'This email address has already been registered.'
      }
    )
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','first_name','last_name']
    is_client = models.BooleanField(
      'client status',
      default=False,
      help_text='Designates whether the user can log into this admin site.'
    )
    is_verified = models.BooleanField(
      'verified status',
      default=True,
      help_text='Designates whether the user has verified their email address.'
    )

    def __str__(self):
        return self.username
    
    def get_short_name(self)->str:
        return super().get_short_name()
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    address = models.CharField(max_length=100)
    country = models.CharField(max_length=50)
    

    def __str__(self):
        return self.user.username
"""