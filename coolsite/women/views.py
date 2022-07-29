from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *

menu = [{'title': "About", 'url_name': "about"},
        {'title': "Add Article", 'url_name': "add_page"},
        {'title': "Contact us", 'url_name': "contact_us"},
        {'title': "Login", 'url_name': "login"}
        ]


# Create your views here.
def index(request):
    posts = Women.objects.all()

    context = {'posts': posts,
               'menu': menu,
               'title': "Main page",
               'cat_selected': 0
               }
    # return HttpResponse("MAIN!!!! New page of application")
    return render(request, "women/index.html", context=context)


def about(request):
    # return HttpResponse("MAIN!!!! New page of application")
    return render(request, "women/about.html", {'menu': menu, 'title': "About"})


def add_page(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST,request.FILES)
        if form.is_valid():
            # print(form.cleaned_data)
            form.save()
            return redirect('home')
    else:
        form = AddPostForm()
    return render(request, 'women/addpage.html', {'form': form, 'menu': menu, 'title': 'Add article'})


def contact_us(request):
    return HttpResponse("Contact us")


def login(request):
    return HttpResponse("Login")


def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Page not found!!!!!!</h1>")


def show_post(request, post_slug):
    post = get_object_or_404(Women, slug=post_slug)
    context = {
        'post': post,
        'menu': menu,
        'title': post.title,
        'cat_selected': post.cat_id,
    }
    return render(request, 'women/post.html', context=context)


def show_category(request, cat_id):
    posts = Women.objects.filter(cat_id=cat_id)
    if len(posts) == 0:
        raise Http404()

    context = {'posts': posts,
               'menu': menu,
               'title': "Show by categories",
               'cat_selected': cat_id
               }
    return render(request, "women/index.html", context=context)
