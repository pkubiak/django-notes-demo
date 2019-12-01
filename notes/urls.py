from django.conf.urls import url

from notes.views import NoteListView, NoteDetailView, NoteCreateView, NoteUpdateView, NoteDeleteView
from notes.views import TopicListView, TopicDetailView, TopicCreateView, TopicUpdateView, TopicDeleteView

from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^$', NoteListView.as_view(), name='note-list'),
    
    url(r'^topics/$', TopicListView.as_view(), name='topic-list'),
    url(r'^topics/(?P<pk>\d+)$', TopicDetailView.as_view(), name='topic-detail'),
    url(r'^topics/add$', login_required(TopicCreateView.as_view()), name='topic-create'),
    url(r'^topics/edit/(?P<pk>\d+)$', login_required(TopicUpdateView.as_view()), name='topic-update'),
    url(r'^topics/delete/(?P<pk>\d+)$', login_required(TopicDeleteView.as_view()), name='topic-delete'),

    url(r'^add/$', login_required(NoteCreateView.as_view()), name='note-create'),
    url(r'^edit/(?P<pk>\d+)/$', login_required(NoteUpdateView.as_view()), name='note-update'),
    url(r'^delete/(?P<pk>\d+)/$', login_required(NoteDeleteView.as_view()), name='note-delete'),
    url(r'^(?P<pk>\d+)/$', NoteDetailView.as_view(), name='note-detail'),
]
