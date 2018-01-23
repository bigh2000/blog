from django.shortcuts import render
from .models import Post

def post_list(request):
    qs = Post.objects.all().order_by('-id')
    return render(request, 'post_list.html', {
        'post_list' : qs,
    })