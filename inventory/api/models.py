from django.db import models


class MyInventory(models.Model):
    name = models.CharField(max_length=128)
    is_deleted = models.BooleanField(default=False)

    def soft_delete(self):
        self.is_deleted = True
        self.save()
