from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=140)
    age = models.IntegerField()
    #login_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}'.format(self.name)

    class Meta:
        #verbose_name_plural = 'Searches'
        ordering = ['name']
