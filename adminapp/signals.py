from adminapp.models import Gallery
from django.utils.text import slugify
from django.db.models.signals import post_save,pre_save
from django.dispatch import receiver



@receiver(pre_save,sender = Gallery)
def gallery_save(sender, instance, *args, **kwargs):
    if not instance.slug:
        print('####### gallery ######')
        instance.slug = slugify(instance.about)
