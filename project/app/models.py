
from cloudinary_storage.storage import MediaCloudinaryStorage,VideoMediaCloudinaryStorage,RawMediaCloudinaryStorage
from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import (
    MaxLengthValidator, MinLengthValidator, EmailValidator,
    MaxValueValidator, MinValueValidator
)
import os



def validate_username(value):
    if not value.replace(' ', '').isalpha():
        raise ValidationError("Username must contain only alphabets and spaces.")


def validate_resume_file(value):
    ext = os.path.splitext(value.name)[1].lower()
    allowed = ['.pdf', '.docx']

    if ext not in allowed:
        raise ValidationError("Resume must be PDF or DOCX.")


def validate_image_file(value):
    ext = os.path.splitext(value.name)[1].lower()
    allowed = ['.jpg', '.jpeg', '.png']

    if ext not in allowed:
        raise ValidationError("Image must be JPG/PNG.")


def validate_password(value):
    if len(value) < 6:
        raise ValidationError("Password must be at least 6 characters long.")
    if not any(c.isdigit() for c in value):
        raise ValidationError("Password must contain at least one number.")
    if not any(c.isalpha() for c in value):
        raise ValidationError("Password must contain at least one alphabet.")


class data(models.Model):
    username = models.CharField(
        max_length=50,
        validators=[validate_username, MinLengthValidator(3)],null=True
    )

    useremail = models.EmailField(
        validators=[EmailValidator()],
        unique=True,          # Important: Avoids duplicate emails
        null=True
    )

    userage = models.IntegerField(
        validators=[MinValueValidator(18), MaxValueValidator(60)],
        null=True
    )

    discription = models.CharField(
        max_length=150,
        validators=[MinLengthValidator(10)]
    )

    resume = models.FileField(
        upload_to='resumes/',
        validators=[validate_resume_file],
        blank=True,
        null=True
    )

    image = models.ImageField(
        upload_to='images/', 
        validators=[validate_image_file],
        null=True,
        blank=True
    )

    password = models.CharField(
        max_length=50,
        validators=[validate_password]
    )

    cpassword = models.CharField(
        max_length=50,
      null=True,
    blank=True

    )

    # Extra model validation
    def clean(self):
        if self.password != self.cpassword:
            raise ValidationError({"cpassword": "Passwords do not match."})

    def __str__(self):
        return self.username


class Upload(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    email = models.EmailField(unique=True)
    photo = models.ImageField(upload_to='images/', storage=MediaCloudinaryStorage())
    video = models.FileField(upload_to='videos/', storage=VideoMediaCloudinaryStorage())