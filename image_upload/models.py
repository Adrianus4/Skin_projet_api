from django.db import models
from PIL import Image
import os

class UploadedImage(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)
        
        # Redimensionar la imagen si es necesario
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

    def delete(self, *args, **kwargs):
        # Eliminar el archivo de imagen al eliminar el objeto
        if os.path.isfile(self.image.path):
            os.remove(self.image.path)
        super().delete(*args, **kwargs)