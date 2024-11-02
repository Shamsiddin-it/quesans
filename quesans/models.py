from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
    

class Subcategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class User(models.Model):
    first_name = models.CharField( max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=100)
    image = models.ImageField(upload_to="static/users/images", height_field=None, width_field=None, max_length=None, null=True, blank=True)
    phone = models.CharField(max_length=13)
    created_on = models.DateField(auto_now=True)

    def __str__(self):
        return self.username

class Question(models.Model):
    title = models.CharField( max_length=50)
    description = models.TextField()
    category = models.ForeignKey(Subcategory, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="static/questions/images",null=True, blank=True)
    file = models.FileField( upload_to="static/questions/files", max_length=100, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateField( auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    
class Answer(models.Model):
    title = models.CharField( max_length=50)
    description = models.TextField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="static/questions/images",null=True, blank=True)
    file = models.FileField( upload_to="static/questions/files", max_length=100, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateField( auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    