# Create your views here.
from django.http import HttpResponse, Http404
from django.template import Context
from django.template.loader import get_template
from django.contrib.auth.models import User
from django.shortcuts import render_to_response
from isobres.models import *
import json#, XMLObject
from forms import *
from json import JSONEncoder
#from django.utils import simplejson
from django.core import serializers
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from rest_framework import generics, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from isobres.serializers import *
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from serializers import *
def mainpage(request):
	return render_to_response(
		'mainpage.html', {
		'titlehead':'Sobres aPP',
		'pagetitle':'Welcome to the sobres application',
		'contentbody':'managing non legalfunding since 2013',
		'user':request.user
		})
	output = template.render(variables)
	return HttpResponse(output)


def review(request, idAlumne):
    print "Genis guapo"
    alumne = get_object_or_404(Alumne, idAlumne=idAlumne)
    review = AlumneReview(
    	rating=request.POST['rating'],
    	comment=request.POST['comment'],
        
        user=request.user,
        alumne=alumne)
    review.save()
    return HttpResponseRedirect(reverse('alumne', args=(alumne.idAlumne,)))






def userpage(request, username):
	try:
		user = User.objects.get(username=username)
	except:
		raise Http404('User not found')
	sobres = user.sobre_set_all()
	template = get_template ('userpage.html')
	variables = Context({
		'username':username,
		'sobres':sobres,

		})
	output = template.render(variables)
	return HttpResponse(output)

def cursList(request):

	try:
		curs = Curs.objects.all()

	
	except:
		raise Http404('Informacio not found')
	template = get_template('cursos.html')
	var = Context({
		'curs':curs,
		'user':request.user
		})

	output = template.render(var)
	return HttpResponse(output)

def profList(request):
	try:
		p = Professor.objects.all()
	except:
		raise Http404('Informacio not found')
	template = get_template('profs.html')
	var = Context({
		'prof':p,
		'user':request.user

		})
	output = template.render(var)
	return HttpResponse(output)

def auList(request):
	try:
		aula = Aula.objects.all()
	except:
		raise Http404('Informacio not found')
	template = get_template('aules.html')
	var = Context({
		'aula':aula,
		'user':request.user
		})
	output = template.render(var)
	return HttpResponse(output)
def alumList(request):
	try:
		alumne = Alumne.objects.all()
	except:
		raise Http404('Informacio not found')
	template = get_template('alums.html')
	var = Context({
		'alumne':alumne,
		'user':request.user
		})
	output = template.render(var)
	return HttpResponse(output)

def titList(request):
	try:
		tit = Titulacio.objects.all()
	except:
		raise Http404('Informacio not found')
	template = get_template('tit.html')
	var = Context({
		'titulacio': tit,
		'user':request.user
		})
	output = template.render(var)
	return HttpResponse(output)



def indexmodel (request, model):
	#print model
	try:
		objectmodel = model.objects.all()
	except:
		raise Http404('Informacio not found')
	template = get_template(model+'.html')
	var = Context({
		model: objectmodel,
		})
	output = template.render(var)
	return HttpResponse(output)

def httpReturn(ficherohtml, key, value ):
	template = get_template(ficherohtml)
	var = Context({
		key: value,
		'titol': 'informacio sobre '+key,
		'capcalera': key,

		})
	output = template.render(var)
	return HttpResponse(output)


def aula (request, aula,xml=None):
	if xml is None:
		try:
			aula = Aula.objects.get(id = aula)
		except:
			raise Http404('Informacio not found')
		return httpReturn("aula.html", 'aula', aula)
	else:
		return xmlResponse(Aula)

def titulacio (request, titulacio, xml=None):
	if xml is None:
		try:
			tit = Titulacio.objects.get(idTitulacio = titulacio)
		except:
			raise Http404('Informacio not found')
		return httpReturn("titulacio.html", 'titulacio', tit)		
	else:
		return xmlResponse(Titulacio)
	
def xmlResponse(model):

	XMLSerializer = serializers.get_serializer("xml")
	xml_serializer = XMLSerializer()
	xml_serializer.serialize(model.objects.all())
	data = xml_serializer.getvalue()
	f = open("xml", "w")
	print >>f, data
	print data
	f.close()
	return HttpResponse(data, content_type="isobres/html+xml")

def alumne(request, alumne, xml=None):

	if xml is None:
		try:
			alu = Alumne.objects.get(idAlumne = alumne)
		except:
			raise Http404('22222222222 not found')
		return httpReturn("alumne.html", 'alumne', alu)
	else:
		return xmlResponse(Alumne)
def curs(request, curs, xml=None):
	if xml is None:
		try:
			curs = Curs.objects.get(idCurs = curs)
		except:
			raise Http404('Informacio not found')
		return httpReturn("curs.html", 'curs', curs)
	else:
		return xmlResponse(Curs)

def professor(request, prof, xml=None):
	if xml is None:
		try:
			prof = Professor.objects.get(idProfessor = prof)
		except:
			raise Http404('Informacio not found')
		return httpReturn("professor.html", 'professor', prof)
	else: 
		return xmlResponse(Professor)






class AlumneDetail (DetailView):
	model = Alumne
	template_name = 'alumne.html'

	def get_context_data(self, **kwargs):
		context = super(AlumneDetail, self).get_context_data(**kwargs)
		return context


class ProfessorDetail (DetailView):
	model = Professor
	template_name = 'professor.html'

	def get_context_data(self, **kwargs):
		context = super(ProfessorDetail, self).get_context_data(**kwargs)
		return context


class AulaDetail (DetailView):
	model = Aula
	template_name = 'aula.html'


	def get_context_data(self, **kwargs):
		context = super(AulaDetail, self).get_context_data(**kwargs)
		return context		

class CursDetail (DetailView):
	model = Curs
	template_name = 'curs.html'

	def get_context_data(self, **kwargs):
		context = super(CursDetail, self).get_context_data(**kwargs)
		return context
class TitulacioDetail (DetailView):
	model = Titulacio
	template_name = 'titulacio.html'

	def get_context_data(self, **kwargs):
		context = super(TitulacioDetail, self).get_context_data(**kwargs)
		return context




class AlumneCreate(CreateView):
	model = Alumne
	print model

	template_name = 'form.html'
	form_class = AlumneForm
	print form_class
	def form_valid(self, form):
		form.instance.user=self.request.user

		return super(AlumneCreate, self).form_valid(form)


class ProfessorCreate(CreateView):
	model = Professor
	template_name = 'form.html'
	form_class = ProfessorForm
	def form_valid(self, form):
		form.instance.user=self.request.user
		return super(ProfessorCreate, self).form_valid(form)



class AulaCreate(CreateView):
	model = Aula
	template_name = 'form.html'
	form_class = AulaForm
	def form_valid(self, form):
		form.instance.user=self.request.user
		return super(AulaCreate, self).form_valid(form)


class CursCreate(CreateView):
	model = Curs
	template_name = 'form.html'
	form_class = CursForm
	def form_valid(self, form):
		form.instance.user=self.request.user
		return super(CursCreate, self).form_valid(form)




class TitulacioCreate(CreateView):
	model = Titulacio
	template_name = 'form.html'
	form_class = TitulacioForm
	def form_valid(self, form):
		form.instance.user=self.request.user
		return super(TitulacioCreate, self).form_valid(form)




class AulaDelete (DeleteView):

	model = Aula
	template_name = 'delete.html'
	success_url = reverse_lazy('auList')

class AlumneDelete (DeleteView):
	model = Alumne
	template_name = 'delete.html'
	success_url = reverse_lazy('alumList')

class TitulacioDelete (DeleteView):
	model = Titulacio
	template_name = 'delete.html'
	success_url = reverse_lazy('titList')

class CursDelete (DeleteView):
	model = Curs
	template_name = 'delete.html'
	success_url = reverse_lazy('cursList')



class APIAulaList(generics.ListCreateAPIView):
	model= Aula
	serializer_class = AulaSerializer

class APIAulaDetail(generics.RetrieveUpdateDestroyAPIView):
	model = Aula
	serializer_class = AulaSerializer

class APIAlumneList(generics.ListCreateAPIView):
	model= Alumne
	serializer_class = AlumneSerializer

class APIAlumneDetail(generics.RetrieveUpdateDestroyAPIView):
	model = Alumne
	serializer_class = AlumneSerializer

class APIProfessorList(generics.ListCreateAPIView):
	model= Professor
	serializer_class = ProfessorSerializer

class APIProfessorDetail(generics.RetrieveUpdateDestroyAPIView):
	model = Professor
	serializer_class = ProfessorSerializer

class APICursList(generics.ListCreateAPIView):
	model= Curs
	serializer_class = CursSerializer

class APICursDetail(generics.RetrieveUpdateDestroyAPIView):
	model = Curs
	serializer_class = CursSerializer

class APITitulacioList(generics.ListCreateAPIView):
	model= Titulacio
	serializer_class = TitulacioSerializer

class APITitulacionsDetail(generics.RetrieveUpdateDestroyAPIView):
	model = Titulacio
	serializer_class = TitulacioSerializer
	
class APIAlumneReviewList(generics.ListCreateAPIView):
	model=AlumneReview
	serializer_class = AlumneReviewSerializer
	
class APIAlumneReviewDetail(generics.RetrieveUpdateDestroyAPIView):
	model = AlumneReview
	serializer_class = AlumneReviewSerializer
	
