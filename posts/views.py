from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator


from .models import Posts
# Create your views here.
def index(request):
    posts = Posts.objects.order_by('-post_date')


    paginator = Paginator(posts, 2)
    page = request.GET.get('page')
    paged_posts = paginator.get_page(page)

    context = {
        'posts' : paged_posts
    }

    return render(request, 'posts/posts.html', context)

def post(request, post_id):

    post = get_object_or_404(Posts, pk=post_id)

    context = {
        'post' : post
    }
    return render(request, 'posts/post.html', context)

def search(request):
    return render(request, 'posts/search.html')