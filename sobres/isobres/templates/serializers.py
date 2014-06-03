from rest_framework.fields import CharField
from rest_framework.relations import HyperlinkedRelatedField, HyperlinkedIdentityField
from rest_framework.serializers import HyperlinkedModelSerializer
from isobres.models import *

class AlumneSerializer(HyperlinkedModelSerializer):
	url = HyperlinkedIdentityField(view_name='alumne-detail')
	Curs = HyperlinkedRelatedField(many=True, read_only=True, view_name='curs-detail')
	alumnereview_set = HyperlinkedRelatedField(many=True, read_only=True, view_name='alumne-detail')
	user = CharField(read_only=True)


	class Meta:
		model = Alumne
		fields = ('url', 'name', 'nif', 'country', 'city', 'curs', 'user', 'alumnereview_set')

class ProfessorSerializer(HyperlinkedModelSerializer):
	url = HyperlinkedIdentityField(view_name='professor-detail')
	curs = HyperlinkedRelatedField(many=True, read_only=True, view_name='curs-detail')
	#user = CharField(read_only=True)

	class Meta:
		model = Professor
		fields = ('url','name', 'nif', 'curs')

class CursSerializer(HyperlinkedModelSerializer):
	url = HyperlinkedIdentityField(view_name='curs-detail')
	titulacio = HyperlinkedRelatedField(many=True, read_only=True, view_name='titulacio-detail')
	user = CharField(read_only=True)

	class Meta:
		model = Curs
		fields = ('url', 'year', 'titulacio', 'user')

class AulaSerializer(HyperlinkedModelSerializer):
	url = HyperlinkedIdentityField(view_name='aula-detail')
	curs= HyperlinkedRelatedField(many=True, read_only=True, view_name='curs-detail')
	user = CharField(read_only=True)

	class Meta:
		model = Aula
		fields = ('url', 'name', 'capacity', 'curs', 'user')

class TitulacioSerializer(HyperlinkedModelSerializer):
	url = HyperlinkedIdentityField(view_name='titulacio-detail')
	user = CharField(read_only=True)

	class Meta:
		model = Titulacio
		fields = ('url', 'name', 'faculty', 'user')

