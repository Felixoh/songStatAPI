from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _ 
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager
from django.conf import settings
from django.db.models.signals import post_save,pre_save
from django.dispatch import receiver

import datetime
from datetime import timedelta
from datetime import datetime as dt
from django.dispatch import receiver

class CustomAccountManager(BaseUserManager):
    def create_superuser(self,email,user_name,first_name,password,**other_fields):
        other_fields.setdefault('is_staff',True)
        other_fields.setdefault('is_superuser',True)
        other_fields.setdefault('is_active',True)

        if other_fields.get('is_staff') is not True:
            raise ValueError('Superuser must be assigned to is_staff=True')
        if other_fields.get('is_staff') is not True:
            raise ValueError('superuser must be assigned to is_superuser=True')
            
        return self.create_user(email,user_name,first_name,password,**other_fields)
    
    def create_user(self,email,user_name,first_name,password,**other_fields):
        if not email:
            raise ValueError("You must provide an email address")
        email = self.normalize_email(email)
        user = self.model(email=email,user_name=user_name,first_name=first_name,**other_fields)
        user.set_password(password)
        user.save()
        return user

# all information about our users :
class NewUser(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(_('email address'),unique=True)
    user_name = models.CharField(max_length=150,unique=True)
    first_name = models.CharField(max_length=150,blank=True)
    start_date = models.DateTimeField(default=timezone.now)
    about = models.TextField(_('about'),max_length=500,blank=True)

    # new users to be created will be inactive and unable to login
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    objects = CustomAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name','first_name']

    def __str__(self):
        return self.user_name
        
class UserSettings(models.Model):
    user = models.OneToOneField(NewUser,on_delete=models.CASCADE,default=None)
    account_verified = models.BooleanField(default=False)
    verified_code = models.CharField(max_length=100,default='',blank=True)
    verification_expires = models.DateField(default=dt.now().date() + timedelta(days=settings.VERIFY_EXPIRE_DAYS)) 
    #will be adding some profile expiration date to the user in the system.
    code_expired = models.BooleanField(default=False)
    receive_email_notice = models.BooleanField(default=True)

    def __str__(self):
        return self.user.user_name

# Membership data
class Membership(models.Model):
    MEMBERSHIP_CHOICES = (
        ('Basic','Basic'),
        ('Advanced','Advance'),
        ('Extended','Extended'),
        ('Premium','Premium'),
        ('Free','Free'),
        ('Medium','Medium')
    )

    PERIOD_DURATION = (
        ('Days','Days'),
        ('Week','Week'),
        ('Months','Months')
    )

    slug = models.SlugField(null=True,blank=True)
    membership_type = models.CharField(choices=MEMBERSHIP_CHOICES,default='Free',max_length=30)
    duration = models.PositiveIntegerField(default=7)
    duration_period = models.CharField(max_length=100,default='Day',choices=PERIOD_DURATION)
    price = models.DecimalField(max_digits=10,decimal_places=2,default=0.00)

    def __str__(self):
        return self.membership_type
        
class PayHistory(models.Model):
    user = models.ForeignKey(NewUser,on_delete=models.CASCADE,null=None)
    amount = models.DecimalField(max_digits=10,decimal_places=2,default=0.00)
    date = models.DateTimeField(auto_now_add=True)
    payment_for = models.ForeignKey(Membership,on_delete=models.SET_NULL,null=True,blank=True)

    def __str__(self):
        return self.user.user_name

class UserMembership(models.Model):
    user = models.OneToOneField(NewUser,related_name="user_membership",on_delete=models.CASCADE)
    membership = models.ForeignKey(Membership,related_name='user_membership',on_delete=models.SET_NULL,null=True)

    def __str__(self):
        return self.user.user_name


# trick play to set the default expiration date to seven days after member has been saved using the signals as shown in  the signal below.
@receiver(post_save,sender=UserMembership)
def create_subscription(sender,instance,*args,**kwargs):
    if instance:
        Subscription.objects.create(user_membership=instance,expires_in=dt.now().date() + timedelta(days=instance.membership.duration))

# User subscription model
class Subscription(models.Model):
    user_membership = models.ForeignKey(UserMembership,related_name='subscription',on_delete=models.CASCADE,default=None)
    expires_in = models.DateField(null=True,blank=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.user_membership.user.user_name

# signal to deactivate user after expriration date.
@receiver(post_save,sender=Subscription)
def update_active(sender,instance,*args,**kwargs):
    today = datetime.date.today()
    if instance.expires_in <= today:
        # delete the subscription from the database when it has expired.
        instance.delete()
