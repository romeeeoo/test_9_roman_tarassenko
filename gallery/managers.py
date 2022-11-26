from django.db.models import Manager


class PictureManager(Manager):
    def all(self):
        return self.get_queryset().order_by('-created_at')
