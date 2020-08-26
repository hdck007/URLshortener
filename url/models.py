from django.db import models

# Create your models here.
class BigUrl(models.Model):
	inputurl = models.URLField(null=True,max_length=200)
	
	def get_absolute_url(self):
	    return reverse('post-detail', kwargs={'pk': self.pk})