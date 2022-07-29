import contact as contact
from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', index, name="home"),
    path('about/', about, name="about"),
    path('addpage/', add_page, name="add_page"),
    path('contact_us/', contact_us, name="contact_us"),
    path('login/', login, name="login"),
    path('post/<slug:post_slug>/', show_post, name="post"),
    path('category/<int:cat_id>/', show_category, name="category"),

    # path('cats/<int:catid>/', categories),
    # re_path(r'^archive/(?P<year>[0-9]{4})', archive)

]
