from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from .forms import *

# menu = [{'title': "About", 'url_name': "about"},
#         {'title': "Add Article", 'url_name': "add_page"},
#         {'title': "Contact us", 'url_name': "contact_us"},
#         {'title': "Login", 'url_name': "login"}
#         ]
from .utils import DataMixin, menu


class WomenHome(DataMixin, ListView):
    model = Women
    template_name = 'women/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Main page")
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Women.objects.filter(is_published=True)


# def index(request):
#     posts = Women.objects.all()
#
#     context = {'posts': posts,
#                'menu': menu,
#                'title': "Main page",
#                'cat_selected': 0
#                }
#     # return HttpResponse("MAIN!!!! New page of application")
#     return render(request, "women/index.html", context=context)


def about(request):
    # return HttpResponse("MAIN!!!! New page of application")
    return render(request, "women/about.html", {'menu': menu, 'title': "About"})


class AddPage(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'women/addpage.html'
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Add article')
        return dict(list(context.items()) + list(c_def.items()))


# def add_page(request):
#     if request.method == 'POST':
#         form = AddPostForm(request.POST, request.FILES)
#         if form.is_valid():
#             # print(form.cleaned_data)
#             form.save()
#             return redirect('home')
#     else:
#         form = AddPostForm()
#     return render(request, 'women/addpage.html', {'form': form, 'menu': menu, 'title': 'Add article'})


def contact_us(request):
    return HttpResponse("Contact us")


def login(request):
    return HttpResponse("Login")


def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Page not found!!!!!!</h1>")


class ShowPost(DataMixin, DeleteView):
    model = Women
    template_name = 'women/post.html'
    slug_url_kwarg = 'post_slug'
    # pk_url_kwarg =
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['post'])
        return dict(list(context.items()) + list(c_def.items()))


# def show_post(request, post_slug):
#     post = get_object_or_404(Women, slug=post_slug)
#     context = {
#         'post': post,
#         'menu': menu,
#         'title': post.title,
#         'cat_selected': post.cat_id,
#     }
#     return render(request, 'women/post.html', context=context)


class WomenCategory(DataMixin, ListView):
    model = Women
    template_name = 'women/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return Women.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Category -' + str(context['posts'][0].cat),
                                      cat_selected=context['posts'][0].cat_id)
        return dict(list(context.items()) + list(c_def.items()))

# def show_category(request, cat_id):
#     posts = Women.objects.filter(cat_id=cat_id)
#     if len(posts) == 0:
#         raise Http404()
#
#     context = {'posts': posts,
#                'menu': menu,
#                'title': "Show by categories",
#                'cat_selected': cat_id
#                }
#     return render(request, "women/index.html", context=context)
