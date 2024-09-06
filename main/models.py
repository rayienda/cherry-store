from django.db import models

class StoreInfo(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()

    @property
    def is_mood_strong(self):
        return self.price > 5