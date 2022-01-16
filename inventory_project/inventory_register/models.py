import uuid
import os
from django.db import models
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile
from django.db.models.signals import post_delete
from django.dispatch import receiver

def inventory_image_file_path(instance, filename):
    """Generate file path fot new image"""
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'

    return os.path.join('inventory/', filename)


class Inventory(models.Model):
    itemname = models.CharField(max_length=100)
    quantity = models.CharField(max_length=100, default = '')
    image = models.ImageField(null=True, upload_to=inventory_image_file_path)


    def save(self, *args, **kwargs):
        self.make_thumbnail()
        super(Inventory, self).save(*args, **kwargs)


    def make_thumbnail(self):
        """store image with thumbnail"""
        image = Image.open(self.image)
        size = (100, 100)
        image.thumbnail(size, Image.ANTIALIAS)

        thumb_name, thumb_extension = os.path.splitext(self.image.name)
        thumb_extension = thumb_extension.lower()

        thumb_filename = thumb_name + '_thumb' + thumb_extension

        if thumb_extension in ['.jpg', '.jpeg']:
            FTYPE = 'JPEG'
        elif thumb_extension == '.gif':
            FTYPE = 'GIF'
        elif thumb_extension == '.png':
            FTYPE = 'PNG'
        else:
            return False    # Unrecognized file type

        # Save thumbnail to in-memory file as StringIO
        temp_thumb = BytesIO()
        image.save(temp_thumb, FTYPE)
        temp_thumb.seek(0)

        # set save=False, otherwise it will run in an infinite loop
        self.image.save(thumb_filename, ContentFile(temp_thumb.read()), save=False)
        temp_thumb.close()

@receiver(post_delete, sender=Inventory)
def delete_upload_files(sender, instance, **kwargs):
    """Delete the upload image"""
    instance.image.delete(False)
