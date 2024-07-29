

# users/models.py
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.conf import settings

class CustomUser(AbstractUser):
    public_visibility = models.BooleanField(default=False)
    birth_year = models.IntegerField(null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)


    groups = models.ManyToManyField(
        Group,
        related_name='customuser_set',  # Add this line
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_set',  # Add this line
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    @property
    def age(self):
        import datetime
        if self.birth_year:
            return datetime.datetime.now().year - self.birth_year
        return None




class UploadedFile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    visibility = models.BooleanField(default=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    year_of_publication = models.IntegerField()
    file = models.FileField(upload_to='uploaded_files/')
    upload_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title



