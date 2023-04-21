from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.

class Ad(models.Model):
    title = models.CharField(
        max_length=200,
        validators=[MinLengthValidator(2, "Title must be greater than 1 character")]
    )
    price = models.PositiveIntegerField()
    text = models.TextField()
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
