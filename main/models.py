from django.db import models

# Create your models here.
class Book(models.Model):
	book_name = models.CharField(max_length=40)
	time_buying = models.DateField(null=True, blank=True)
	def __unicode__(self):
		return self.book_name
