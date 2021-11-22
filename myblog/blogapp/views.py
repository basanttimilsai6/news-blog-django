from django.shortcuts import render
from .models import post
# Create your views here.
def bloghome(request):
    allpost = post.objects.all()
    params = {'allpost':allpost}
    return render(request, 'blog/bloghome.html',params)


def blogpost(request, slug):
    Post = post.objects.filter(slug=slug).first()
    context = {'Post':Post}

    return render(request, 'blog/blogpost.html', context)