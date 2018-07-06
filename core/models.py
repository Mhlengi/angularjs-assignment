import logging

from django.db import models
from jsonfield import JSONField


class Carousel(models.Model):
    title = models.CharField(max_length=75)
    description = models.TextField(blank=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class OutSourceTask(models.Model):
    description = JSONField()
    is_completed = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        super(OutSourceTask, self).save(*args, **kwargs)
        update_carousel(self.description)


def update_carousel(description):
    if description:
        try:
            if 'Carousel' in description:
                for title in description['Carousel']:
                    Carousel.objects.get_or_create(title=title)
        except Exception as e:
            logging.error(e)
