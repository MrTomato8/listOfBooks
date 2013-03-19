from django.db import models


class Books(models.Model):
    name = models.CharField(max_length=100, verbose_name="Name")
    description = models.CharField(max_length=100, verbose_name="Description")
    author = models.CharField(max_length=100, verbose_name="Author")

    def _unicode__(self):
        return u'%s %s' % (self.name, self.author)
