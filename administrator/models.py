from django.db import models
from django.core.validators import FileExtensionValidator

# Create your models here.

class MediaModel(models.Model):
    attach = models.FileField(
            # upload_to='uploads/%Y/%m/%d/',
            upload_to='xlsx/',
            validators=[FileExtensionValidator(['xlsx', ])],
        )
    def __str__(self):
        return self.attach.url