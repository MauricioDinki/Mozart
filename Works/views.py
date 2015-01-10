from .models import Work
from django.http import JsonResponse
from django.shortcuts import render,get_list_or_404
from django.views.generic import ListView

class WorkListView(ListView):
    model = Work
    template_name = "work_list.html"
    context_object_name = 'works'

    def get(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        data = [{
	        'user': Work.user.username,
	        'title':Work.title,
	        'category':Work.category,
	        'date':Work.date,
	        'cover':Work.cover.url,
	        'archive':Work.archive.url,
        } for Work in self.object_list]
    	return JsonResponse(data,safe=False)

    def get_queryset(self):
        if self.kwargs.get('category'):
            queryset = get_list_or_404(self.model,category=self.kwargs['category'])
        else:
            queryset = super(WorkListView, self).get_queryset()
        return queryset

