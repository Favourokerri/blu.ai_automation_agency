from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Hero_section(models.Model):
    title=models.CharField(max_length=50, help_text="enter title")
    body=models.CharField(max_length=200, help_text="enter body")
    image= models.ImageField(upload_to="heros", blank=True, null=True)

class About_us(models.Model):
    about=RichTextField(default="about us")

class MainServices(models.Model):
    description=RichTextField(default="about service")

class Services(models.Model):
    name_of_service=models.CharField(max_length=200, help_text="enter name of service")
    about_service=RichTextField(default="about us")
    date_posted=models.DateTimeField(auto_now_add=True)

class Team(models.Model):
    name=models.CharField(max_length=100, default="blueai_worker", help_text="enter your name")
    image=models.ImageField(upload_to="team", blank=True, null=True)
    position=models.CharField(max_length=200)
    about=models.CharField(max_length=300)
    twitter=models.URLField(
        verbose_name="Twitter Link",
        max_length=200,  # Adjust the maximum length based on your needs
        blank=True,
        null=True,
        help_text="Enter your Twitter profile link here."
    )

    facebook=models.URLField(
        verbose_name="Facebook Link",
        max_length=200,  # Adjust the maximum length based on your needs
        blank=True,
        null=True,
        help_text="Enter your Twitter profile link here."
    )

    instagram = models.URLField(
        verbose_name="Instagram Link",
        max_length=200,  # Adjust the maximum length based on your needs
        blank=True,
        null=True,
        help_text="Enter your Twitter profile link here."
    )

    linkedln = models.URLField(
        verbose_name="Linkedln Link",
        max_length=200,  # Adjust the maximum length based on your needs
        blank=True,
        null=True,
        help_text="Enter your Twitter profile link here."
    )

class Questions(models.Model):
    question=models.CharField(max_length=300)
    answer=models.CharField(max_length=500)

class Details(models.Model):
    """details about bluai"""
    location=models.CharField(max_length=300)
    email=models.CharField(max_length=200)
    phone_number=models.CharField(max_length=20)

class Contact_Us(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField()
    subject=models.CharField(max_length=200)
    message=models.CharField(max_length=700)
    replied=(
        ('r', 'replied'),
        ('n', 'new_message'),
    ) 

    replied_status=models.CharField(max_length=20, choices=replied, default='n', blank=True, null=True)

class Accounts(models.Model):
    twitter=models.URLField(
        verbose_name="Twitter Link",
        max_length=200,  # Adjust the maximum length based on your needs
        blank=True,
        null=True,
        help_text="Enter your Twitter profile link here."
    )

    facebook=models.URLField(
        verbose_name="Facebook Link",
        max_length=200,  # Adjust the maximum length based on your needs
        blank=True,
        null=True,
        help_text="Enter your Twitter profile link here."
    )

    instagram = models.URLField(
        verbose_name="Instagram Link",
        max_length=200,  # Adjust the maximum length based on your needs
        blank=True,
        null=True,
        help_text="Enter your Twitter profile link here."
    )

    linkedln = models.URLField(
        verbose_name="Linkedln Link",
        max_length=200,  # Adjust the maximum length based on your needs
        blank=True,
        null=True,
        help_text="Enter your Twitter profile link here."
    )
