from pydoc import describe
from pyexpat import model
from unicodedata import category
from django.db import models
from django.contrib.auth.models import User

USER_TYPE_CHOICES = (
    ("admin", "Admin"),
    ("user", "User")
)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(
                    max_length = 5,
                    choices = USER_TYPE_CHOICES,
                    default = 'user'
                    )



class Category(models.Model):
    category_name = models.CharField(max_length=100,null=False,blank=False)
    description = models.CharField(max_length=255)

    def __str__(self):
        return self.category_name


JOB_LENGTH = (
    ("Less Then 6 Month", "Less Then 6 Month"),
    ("More Then 6 Month", "More Then 6 Month")
)

class Job(models.Model):
    name = models.CharField(max_length=100,null=False,blank=False)
    description = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_by = models.ForeignKey(Profile, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    posting_date = models.DateTimeField(auto_now=True)
    length = models.CharField(
                    max_length = 20,
                    choices = JOB_LENGTH,
                    default = 'less then 6 month'
                    )

    def __str__(self):
        return self.name