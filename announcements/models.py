from django.db import models

class Announcement(models.Model):
    title = models.CharField(max_length=200, default="Genel Duyuru: ")
    textField = models.TextField(null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title






