from django.shortcuts import render
from django.http import HttpResponse
from posts.models import Posts
from blogger.models import Blogger
from django.core.paginator import Paginator
# Create your views here.
def index(request):
    posts = Posts.objects.order_by('-post_date') 
    paginator = Paginator(posts, 2)
    page = request.GET.get('page')
    paged_posts = paginator.get_page(page)

    context = {
        'posts' : paged_posts
    }
    return render(request, 'pages/index.html', context)

def about(request):

    #GEt allblogger

    bloggers = Blogger.objects.all()
 
    #Get mvp


    context = {
        'bloggers':bloggers
        
    }
    return render(request, 'pages/about.html' , context)