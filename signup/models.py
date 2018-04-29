from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
import random

class UserManager(BaseUserManager):
    def create_user(self, email, first_name, sem, last_name, contact, department, degree, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')
        vericd = random.randrange(100000, 999999, 2)
        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            contact=contact,
            degree=degree,
            department=department,
            sem=sem,
            vericode=str(vericd)
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, contact, department, sem, degree, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.create_user(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            contact=contact,
            degree=degree,
            department=department,
            password=password,
            sem=sem,

        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    # /date_of_birth = models.DateField(blank=True,)
    # mobilenumber = RegexValidator(regex=r'^\d{10}$', message="Phone number must be entered in the format: '999999999'. 10 digits allowed.")
    phone_regex = RegexValidator(regex=r'^\d{10}$',
                                 message="Phone number must be entered in the format: '999999999'. 10 digits allowed.")
    contact = models.CharField(max_length=10, validators=[phone_regex], blank=False)
    # mobilenumber=models.IntegerField(unique=True,default=None)
    is_admin = models.BooleanField(default=False)
    first_name = models.CharField(max_length=20, default=None)
    last_name = models.CharField(max_length=10, default=None)

    degree=models.CharField(max_length=50,default=None,choices=(('Bachelors of Technology','B-Tech'),('Masters of Technology','mtech'),('integerated dual degree','idd'),('integerated masters degree','imd')))
    department=models.CharField(max_length=55,default=None,choices=(('Computer Science and Engg.','cse'),('Mathematics and Computing','mnc'),('Electronics Engg.','ece'),('Electrical Engg.','eee')))
    sem = models.CharField(max_length=2,default=None,choices=(('I', '1'), ('II', '2'), ('III', '3'),('IV', '4')))
    vericode = models.CharField(max_length=10, default=None)
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'contact', 'department', 'last_name', 'sem', 'degree']

    def get_full_name(self):
        # The user is identified by their email address
        return self.first_name + self.last_name

    def get_short_name(self):
        # The user is identified by their email address
        return self.first_name

    def __str__(self):  # __unicode__ on Python 2
        return self.first_name + self.last_name

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

