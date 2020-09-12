from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .models import Post

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'list_by_date'

    def get_queryset(self):     #METHOD FOR RETURNING QUERY_SET !!!! LIKELY RETURN MULTIPLE
        return Post.objects.order_by('-created_date')

class AboutView(generic.DetailView):
    template_name = 'polls/about.html'

# Create your views here.