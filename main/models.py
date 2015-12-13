from django.db import models

# Create your models here.

class Category(models.Model):
	name = models.CharField(max_length=30)
#	book = models.ManyToManyField(Book)
	def __unicode__(self):
		return self.name


class Book(models.Model):
	book_name = models.CharField(max_length=40)
	time_buying = models.DateField(null=True, blank=True)
	category = models.ManyToManyField(Category)

	def __unicode__(self):
		return self.book_name
		# return "%s %s" % (self.book_name, self.category.name)
