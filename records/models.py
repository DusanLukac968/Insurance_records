from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.
class Insurance(models.Model):
    """ 
    types of insurances what is insured
    about_insurance: shord description of an insurance
    """
    type_of_insurance = models.CharField(max_length=300, verbose_name="type_of_insurance")
    about_insurance = models.CharField(max_length=600, default="" ,verbose_name="about_insurance")
    
    def __str__(self):
        return "Insurance: {0}".format(self.type_of_insurance)
    
    class Meta:
        verbose_name = "Insurance"
        verbose_name_plural = "Insurances"


class UserManager(BaseUserManager):
    """
    creat regular user and admin 
    """

    def create_user(self, name, surname, age, tel_number, email, password):
        print(self)
        if name and surname and age and tel_number and email and password:
            user = self.model(email=self.normalize_email(email))
            user.set_password(password)
            user.save()
            return user
        
    def create_superuser(self, name, surname, age, tel_number, email, password):
        user = self.create_user(name, surname, age, tel_number, email, password)
        user.is_admin = True
        user.save()
        return user 
    
class User(AbstractBaseUser):
    """
    regular user with name, surname, age, telephone number, email adress,
    regular user is not admin!
    insurance = is user personal insurance/ it's product
    insurance_value = is price on how much is hight of insurance
    """
    name = models.CharField(max_length=300)
    surname = models.CharField(max_length=300)
    age = models.PositiveIntegerField(blank=True, null=True, default=0)
    tel_number = models.CharField(max_length=12)
    email = models.EmailField(max_length=300, unique=True)
    is_admin = models.BooleanField(default=False)
    insurance = models.ForeignKey(Insurance, default="", on_delete=models.SET_NULL, null=True, verbose_name="Insurance")
    insurance_value = models.FloatField(max_length=600, default=0, verbose_name='insurance_value')
    class Meta:
        verbose_name = "user"
        verbose_name_plural ="users"

    objects = UserManager()

    USERNAME_FIELD = "email"
    
    def __str__(self):
        return "email: {0}\n name: {1}\n surname: {2}\n age: {3}\n telephone number: {4}".format(self.email, self.name, self.surname, self.age, self.tel_number)
    
    @property
    def is_staff(self):
        return self.is_admin
    
    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, app_label):
        return True



