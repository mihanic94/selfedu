from django.urls import path, re_path
from women.views import *

urlpatterns = [
    path('', WomenHome.as_view(), name='home'),  # http://127.0.0.1:8000/
    path('about/', about, name='about'),
    path('addpage/', addpage, name='add_page'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>/', WomenCategory.as_view(), name='category'),

    path('cats/<int:catid>/', categories, name='categories'),  # http://127.0.0.1:8000/cats/<catid>/
    re_path(r'^archive/(?P<year>[0-9]{4})/', archive),  # В этой функции можно использовать регулярные выражения.
    path('test1/', test1, name='test1'),
    path('test2/', test2, name='test2'),
]
