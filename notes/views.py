from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin


from notes.models import Note, Topic
import time


class NoteListView(ListView):
    model = Note


class NoteDetailView(DetailView):
    model = Note


class NoteCreateView(CreateView):
    model = Note
    fields = ['title', 'body', 'topic']

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.published_at = time.strftime('%Y-%m-%d %H:%M')
        print(time.strftime('%Y-%m-%d %H:%M'))
        print(form)
        print('*'*100)
        return super().form_valid(form)


class NoteUpdateView(UserPassesTestMixin, UpdateView):
    model = Note
    fields = ['title', 'body', 'topic']

    def test_func(self):
        return self.request.user == self.get_object().author


class NoteDeleteView(UserPassesTestMixin, DeleteView):
    model = Note
    success_url = reverse_lazy('note-list')

    def test_func(self):
        return self.request.user.is_staff or (self.request.user == self.get_object().author)

########################################################################################################

class TopicListView(ListView):
    model = Topic


class TopicDetailView(DetailView):
    model = Topic


class TopicCreateView(CreateView):
    model = Topic
    fields = ['title', 'description', 'public', 'parent']


class TopicUpdateView(UpdateView):
    model = Topic
    fields = ['title', 'description', 'public', 'parent']

class TopicDeleteView(DeleteView):
    model = Topic
    success_url = reverse_lazy('topic-list')
