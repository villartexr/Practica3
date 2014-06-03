from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from datetime import date

def get_default_user():
	return User.objects.get(pk=1)

class Titulacio(models.Model):
	name = models.CharField (max_length=40)
	faculty = models.CharField(max_length=20)
	user = models.ForeignKey(User, default=get_default_user)
	def __unicode__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('titulacio', kwargs={'pk':self.pk})

class Curs(models.Model):
	year = models.IntegerField(max_length=1)
	titulacio = models.ForeignKey(Titulacio)
	user = models.ForeignKey(User, default=get_default_user)
	def __unicode__(self):
		return str(self.year)+" - "+self.titulacio.name
	def get_absolute_url(self):
		return reverse('curs' , kwargs={'pk':self.pk})


class Professor(User):
	name = models.CharField(max_length=40)
	nif = models.IntegerField(max_length=8)
	curs = models.ManyToManyField(Curs)
	#user = models.ForeignKey(User, unique = True)

	def __unicode__(self):
		return self.name
	def get_absolute_url(self):
		return reverse('professor_detail', kwargs={'pk':self.pk})


class Aula(models.Model):
	name = models.CharField(max_length=20)
	capacity = models.IntegerField()
	curs = models.ForeignKey(Curs)
	user = models.ForeignKey(User, default=get_default_user)
	
	def __unicode__(self):
		return self.name
	def get_absolute_url(self):
		return reverse('aula', kwargs={'pk':self.pk})


	# kwargs={'idAula':self.pk}
	#def get_absolute_url(self):
	#	return reverse('Aula:Aula')

class Alumne(models.Model):
	idAlumne = models.AutoField(primary_key=True)
	name = models.CharField(max_length=40)
	nif = models.IntegerField(max_length=8)
	country = models.CharField(max_length=60)
	city = models.CharField(max_length=60)
	curs = models.ManyToManyField(Curs)
	user = models.ForeignKey(User, default=get_default_user)
	def __unicode__(self):
		return self.name
	def get_absolute_url(self):
		#return "alumnesinfo/%i/" % self.id

		return reverse('alumne', kwargs={'pk':self.pk})
	def averageRating(self):
		ratingSum = 0.0
		for review in self.alumnereview_set.all():
			ratingSum += review.rating
		reviewCount = self.alumnereview_set.count()
		return ratingSum/reviewCount
		#fer en el serializers el alumnereview_set
		

class Review (models.Model):
	RATING_CHOICES = ((1,'1'),(2,'2'),(3,'3'),(4,'4'),(5,'5'),(6,'6'),(7,'7'),(8,'8'),(9,'9'),(10,'10'))
<<<<<<< HEAD
	rating = models.PositiveSmallIntegerField('Ratings (stars)', blank=True, default=5, choices=RATING_CHOICES)
=======
	rating = models.PositiveSmallIntegerField('Ratings (stars)', blank=False, default=5, choices=RATING_CHOICES)
>>>>>>> 3061a37bf6c9ee03a76a5fc1edad3a42d18c258d
	comment = models.TextField(blank=True, null=True)
	user = models.ForeignKey(User, default=get_default_user)
	date = models.DateField(default=date.today)
	
	class Meta:
		abstract = True
		
class AlumneReview (Review):
	alumne = models.ForeignKey(Alumne)

