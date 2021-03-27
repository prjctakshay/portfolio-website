from django.db import models

# user details contain this table
class User(models.Model):
    profile_pic = models.ImageField(
        upload_to='user/profile_pic', null=True, blank=True)
    name = models.CharField(max_length=50)
    profession = models.CharField(max_length=100)
    bio_heading = models.CharField(max_length=200)
    bio = models.TextField(max_length=400)


# social media links contain this table
class SocialMedias(models.Model):
    facebook = models.URLField(null=True,blank=True)
    linkedin = models.URLField(null=True,blank=True)
    github = models.URLField(null=True,blank=True)
    instagram = models.URLField(null=True,blank=True)
    whatsapp = models.URLField(null=True,blank=True)


# skills details contain thhis table
class Skills(models.Model):
    image = models.ImageField(upload_to='user/skills', null=True, blank=True)
    heading = models.CharField(max_length=100)
    short_description = models.TextField(max_length=500)


# education details contain this table
class Education(models.Model):
    qualification = models.CharField(max_length=300)
    institute = models.CharField(max_length=150)
    year_start = models.DateField(auto_now=False)
    year_end = models.DateField(auto_now=False)
    mark = models.CharField(max_length=100)


# works details contain this table
class Works(models.Model):
    work_img = models.ImageField(upload_to='user/works', null=True)
    work_title = models.CharField(max_length=100)
    short_discription = models.TextField(max_length=300)
    git_url = models.URLField(null=True)
    website_url = models.URLField(null=True)


# experience details contain this table
class Experience(models.Model):
    position = models.CharField(max_length=150)
    company_name = models.CharField(max_length=150)
    year_start = models.DateField(auto_now=True)
    year_end = models.DateField(auto_now=True, null=True)
    short_description = models.TextField(max_length=500)
    
# contact me details
class ContactMe(models.Model):
    name = models.CharField(max_length=100)
    mail = models.EmailField()
    message = models.TextField(max_length=400)
    # phone_num = PhoneNumberField(null=True)
    phone_num = models.CharField(max_length=12)
    time = models.DateTimeField(auto_now=True)
