from django.db import models


class AbstractCreateUpdateModel(models.Model):
    """
    id, created_at, updated_at abstract model
    """
    id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

    def __str__(self):
        return str(self.id)
