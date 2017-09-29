from django.conf.urls import url, include
from simplemooc.courses import views as coursesViews

urlpatterns = [
    url(r'^$', coursesViews.index, name='index'),
    # url(r'^(?P<pk>\d+)/$', coursesViews.details, name='details'),
    url(r'^(?P<slug>[\w_-]+)/$', coursesViews.details, name='details'),
    url(r'^(?P<slug>[\w_-]+)/inscricao/$', coursesViews.enrollment, name='enrollment'),
    url(r'^(?P<slug>[\w_-]+)/cancelar-inscricao/$', coursesViews.undo_enrollment,
    	name='undo_enrollment'),
    url(r'^(?P<slug>[\w_-]+)/anuncios/$', coursesViews.announcements,
    	name='announcements'),
    url(r'^(?P<slug>[\w_-]+)/anuncios/(?P<pk>\d+)/$', coursesViews.show_announcement,
    	name='show_announcement'),
    url(r'^(?P<slug>[\w_-]+)/aulas/$', coursesViews.lessons, name='lessons'),
    url(r'^(?P<slug>[\w_-]+)/aulas/(?P<pk>\d+)/$', coursesViews.lesson, name='lesson'),
    url(r'^(?P<slug>[\w_-]+)/materiais/(?P<pk>\d+)/$', coursesViews.material, name='material'),
]