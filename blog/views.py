from django.shortcuts import render,get_object_or_404
from .models import blog_model

def Blog_home(request):
    bloger=blog_model.objects.all()
    return render(request, 'blog/blogpage.html', {'bloger':bloger})

def Blog_id(request,abc):
    efg=get_object_or_404(blog_model, pk=abc)
    return render(request, 'blog/selected.html', {'efg':efg})
