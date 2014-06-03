from django.forms import ModelForm
from isobres.models import *

class AlumneForm (ModelForm):

	class Meta:
		model = Alumne

		exclude = ('user',)
		

class AulaForm (ModelForm):
	class Meta:
		model = Aula
		exclude = ('user',)

class ProfessorForm(ModelForm):
	class Meta:
		model = Professor
		exclude = ('user', )

class CursForm (ModelForm):
	class Meta:
		model = Curs
		exclude = ('user', )


class TitulacioForm (ModelForm):
	class Meta:
		model = Titulacio
		exclude = ('user', )




