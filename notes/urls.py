from django.conf.urls import url

from notes.views import NoteListView, NoteDetailView, NoteCreateView, NoteUpdateView, NoteDeleteView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^$', NoteListView.as_view(), name='note-list'),
    url(r'^add/$', login_required(NoteCreateView.as_view()), name='note-create'),
    url(r'^edit/(?P<pk>\d+)/$', login_required(NoteUpdateView.as_view()), name='note-update'),
    url(r'^delete/(?P<pk>\d+)/$', login_required(NoteDeleteView.as_view()), name='note-delete'),
    url(r'^(?P<pk>\d+)/$', NoteDetailView.as_view(), name='note-detail'),
]
