from django.db import models
from django.contrib.auth.models import AbstractBaseUser,  BaseUserManager

# Create your models here.

class MyUserManager(BaseUserManager):
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
            **extra_fields
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

BLOOD_GROUP = sorted([
        ('A+','A+'),
        ('A-','A-'),
        ('B+','B+'),
        ('B-','B-'),
        ('AB+','AB+'),
        ('AB-','AB-'),
        ('O+','O+'),
        ('O-','O-')
    ])

GENDER_CHOICE = [
    ('M', 'Male'),
    ('F','Female'),
    ('Oth','Other')
]

def upload_to(instance, filename):
    return 'avatar/{filename}'.format(filename=filename)

class Profile(models.Model):
    name = models.CharField(max_length=200,blank=False,null=False)
    gender = models.CharField(choices=GENDER_CHOICE,max_length=6, blank=False)
    dob = models.DateField(blank=False,null=False)
    blood_group = models.CharField(choices=BLOOD_GROUP,max_length=3)
    address = models.CharField(max_length=500,blank=False)
    mobile = models.CharField(max_length=20, unique=True)
    avatar = models.ImageField(upload_to=upload_to,null=True,blank=True)
    user = models.OneToOneField(MyUser,on_delete=models.CASCADE,primary_key=True)


    def __str__(self):
        return "%s - %s" % (self.user.email,self.name)




