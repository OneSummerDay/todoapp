from django.db import models

# Create your models here.


class ToDo(models.Model):
    title = models.CharField('Task name', max_length=300)
    is_complete = models.BooleanField('Done', default=False)

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
