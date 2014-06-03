from django.conf.urls import patterns, include, url
from django.contrib.auth.models import User, Group 
from django.db import models
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from isobres.views import *
from isobres.models import *
from isobres.forms import *
from rest_framework import viewsets, routers
from django.views.generic import DetailView, ListView, UpdateView, CreateView

from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.views.generic import DetailView, ListView, UpdateView
from isobres.serializers import *
from rest_framework.urlpatterns import format_suffix_patterns





admin.autodiscover()

class AlumneViewSet(viewsets.ModelViewSet):
    model = Alumne

class TitulacioViewSet(viewsets.ModelViewSet):
    model = Titulacio

class CursViewSet(viewsets.ModelViewSet):
    model = Curs

class AulaViewSet(viewsets.ModelViewSet):

    model = Aula

class ProfessorViewSet(viewsets.ModelViewSet):
   
    model = Professor

router = routers.DefaultRouter()
router.register(r'alumnes', AlumneViewSet)
router.register(r'titulacions', TitulacioViewSet)
router.register(r'cursos', CursViewSet)
router.register(r'aules', AulaViewSet)
router.register(r'professors', ProfessorViewSet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sobres.views.home', name='home'),
    # url(r'^sobres/', include('sobres.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^a', include(router.urls)),
    url(r'^api-restful/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', mainpage, name='home'),
    url(r'^user/(\w+)/$', userpage),
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout'),
    


    url(r'^cursos/$', cursList, name='cursList'),

    url(r'^aules/$', auList, name='auList'),
    url(r'^titulacions/$', titList, name= 'titList'),
    url(r'^alumnes/$', alumList, name='alumList'),
    url(r'^professors/$', profList, name = 'profList'),



    url(r'^aules/create/$', AulaCreate.as_view(), name='aula_create'),
    url(r'^professors/create/$', ProfessorCreate.as_view(), name='professor_create'),
    url(r'^alumnes/create/$', AlumneCreate.as_view(), name='alumne_create'),
    url(r'^titulacions/create/$', TitulacioCreate.as_view(), name='titulacio_create'),
    url(r'^cursos/create/$', CursCreate.as_view(), name='curs_create'),
    
    url(r'^aules/(?P<pk>\d+)$',AulaDetail.as_view(), name='aula'),
    url(r'^professors/(?P<pk>\d+)$',ProfessorDetail.as_view(), name='professor'),
    url(r'^alumnes/(?P<pk>\d+)$',AlumneDetail.as_view(), name='alumne'),
    url(r'^titulacions/(?P<pk>\d+)$',TitulacioDetail.as_view(), name='titulacio'),
    url(r'^cursos/(?P<pk>\d+)$',CursDetail.as_view(), name='curs'),

    url(r'^aules/(?P<pk>\d+)/edit/$',
        UpdateView.as_view(model = Aula, 
        template_name = 'form.html',
        form_class = AulaForm), name='aula_edit'),
    url(r'^professors/(?P<pk>\d+)/edit/$',
        UpdateView.as_view(model= Professor,
        template_name = 'form.html',
        form_class=ProfessorForm), name='professor_edit'),
    url(r'^alumnes/(?P<pk>\d+)/edit/$',
        UpdateView.as_view(model=Alumne,
        template_name = 'form.html',
        form_class = AlumneForm), name='alumne_edit'),
    url(r'^titulacions/(?P<pk>\d+)/edit/$',
        UpdateView.as_view(model = Titulacio,
        template_name = 'form.html',
        form_class = TitulacioForm), name='titulacio_edit'),
    url(r'^cursos/(?P<pk>\d+)/edit/$',
        UpdateView.as_view(model = Curs,
        template_name = 'form.html',
        form_class = CursForm), name='curs'),

       
    # al loro que s'ha de modificar



    url(r'^aules/(?P<pk>\d+)/delete/$',
        AulaDelete.as_view(), 
        name='aula_delete'),

    url(r'^alumnes/(?P<pk>\d+)/delete/$',
        AlumneDelete.as_view(), 
        name='alumne_delete'),

    url(r'^titulacions/(?P<pk>\d+)/delete/$',
        TitulacioDelete.as_view(), 
        name='titulacio_delete'),

    url(r'^cursos/(?P<pk>\d+)/delete/$',
        CursDelete.as_view(), 
        name='curs_delete'),


    url(r'^alumnes/(?P<idAlumne>\d+)/reviews/create$',review, name='review_create'),






    #url(r'^cursos/(\w+)/$', curs),
    #url(r'^professors/(\w+)/$', professor),
    #url(r'^aules/(\w+)/$', aula),
    #url(r'^alumnes/(\w+)/$', alumne),
    #url(r'^titulacions/(\w+)/$', titulacio),

    #(?P<pk>\d+)

    #info xml i json
    url(r'^titulacionsinfo/(\w+)/(\w+)/$', titulacio),
    url(r'^aulesinfo/(\w+)/(\w+)/$', aula),
    url(r'^alumnesinfo/(\w+)/(\w+)/$', alumne),
    url(r'^cursinfo/(\w+)/(\w+)/$', curs),
    url(r'^professorsinfo/(\w+)/(\w+)/$', professor),
)


urlpatterns += patterns('',
    url(r'^api/aules/$',APIAulaList.as_view(), name = 'aula-list'),
    url(r'^api/aules/(?P<pk>\d+)$',APIAulaDetail.as_view(), name = 'aula-detail'),
    url(r'^api/titulacions/$',APIAulaList.as_view(), name = 'titulacions-list'),
    url(r'^api/titulacions/(?P<pk>\d+)$',APITitulacionsDetail.as_view(), name = 'titulacions-detail'),
    url(r'^api/alumnes/$',APIAlumneList.as_view(), name = 'alumnes-list'),
    url(r'^api/alumnes/(?P<pk>\d+)$',APIAlumneDetail.as_view(), name = 'alumnes-detail'),
    url(r'^api/cursos/$',APICursList.as_view(), name = 'cursos-list'),
    url(r'^api/cursos/(?P<pk>\d+)$',APICursDetail.as_view(), name = 'cursos-detail'),
    url(r'^api/professors/$',APIProfessorList.as_view(), name = 'professors-list'),
    url(r'^api/professors/(?P<pk>\d+)$',APIProfessorDetail.as_view(), name = 'professors-detail'),
    url(r'^api/alumnereview/$', APIAlumneReviewList.as_view(), name='alumnereview-list'),
    url(r'^api/alumnereviews/(?P<idAlumne>\d+)/$', APIAlumneReviewDetail.as_view(), name='alumnereview-detail'),

    )

#urlpatterns = format_suffix_patterns(urlpatterns, allowed=['api' ,'json', 'xml'])
