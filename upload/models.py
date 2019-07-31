from django.db import models

class UploadImage(models.Model):
    image = models.ImageField(upload_to="image", max_length=254, blank=True, null=True)

    def __str__(self):
        return self.image
