from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Entry

# Create your views here.
class HomeView(ListView):
	model = Entry
	template_name='entries/index.html'
	context_object_name = 'blog_entries'

class EntryView(DetailView):
	model = Entry
	template_name = 'entries/entry_detail.html'