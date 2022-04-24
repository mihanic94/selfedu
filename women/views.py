from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, DetailView

from women.forms import AddPostForm
from women.models import Women

menu = [{'title': 'О сайте', 'url_name': 'about'},
        {'title': 'Добавить статью', 'url_name': 'add_page'},
        {'title': 'Обратная связь', 'url_name': 'contact'},
        {'title': 'Войти', 'url_name': 'login'},
        ]

class WomenHome(ListView):
    model = Women  # Выбираются все записи из таблицы Women и отображаются в виде списка(имя 'object_list' в шаблоне)
    template_name = 'women/index.html'  # Если не указать этот атрибут, тогда ищется шаблон по адресу: <имя_приложения>/<имя_модели_list.html>
    context_object_name = 'posts'  # Если не использовать этот атрибут, то в шаблоне коллекция будет доступна по имени object_list!
    extra_context = {'title': 'главная страница'}  # Можно передавать только неизменяемые объекты(числа, строки и т.д.)

    def get_context_data(self, *, object_list=None, **kwargs):  # Можно передавать объекты и изменяемые, и неизменяемые
        context = super().get_context_data(**kwargs)  # здесь context ссылается на словарь, в котором уже есть posts и title
        context['menu'] = menu
        context['cat_selected'] = ''
        return context

    def get_queryset(self):
        return Women.objects.filter(is_published=True)


# def index(request):  # request - обязательный аргумент(это ссылка на экземпляр класса HttpRequest). Это ссылка на класс HttpRequest.
#                      # Через request доступна вся информация о текущем запросе.
#     return HttpResponse('Главная страница приложения women')
# def index(request):
#     # print(dir(request))
#     posts = Women.objects.all()
#
#     context = {'menu': menu,
#                'title': 'Главная страница',
#                'posts': posts,
#                'cat_selected': ''
#                }
#
#     return render(request, 'women/index.html', context=context)


def about(request: WSGIRequest):  # Таким образом мы увидим все методы объекта request
    return render(request, 'women/about.html', {'title': 'Заголовок', 'menu': menu})


def addpage(request):
    form = AddPostForm()

    return render(request, 'women/addpage.html', context={'form': form, 'menu': menu, 'title': 'Добавление статьи'})


def contact(request):
    return HttpResponse('Страница с контактными данными')


def login(request):
    return HttpResponse('Страница входа в личный кабинет')


# def show_post(request, post_slug):
#     post = get_object_or_404(Women, slug=post_slug)
#
#     context = {
#         'post': post,
#         'menu': menu,
#         'title': post.title,
#         'cat_selected': post.cat,
#     }
#
#     return render(request, 'women/post.html', context=context)

class ShowPost(DetailView):
    model = Women
    template_name = 'women/post.html'
    slug_url_kwarg = 'post_slug'
    # pk_url_kwarg = <имя параметра>  # Если используем число
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Страница поста'
        return context




# def show_category(request, cat_slug):
#     posts = Women.objects.filter(cat__slug=cat_slug)
#
#     if len(posts) == 0:
#         raise Http404
#
#     context = {'menu': menu,
#                'title': 'Страница категории',
#                'posts': posts,
#                'cat_selected': cat_slug
#                }
#
#     return render(request, 'women/index.html', context=context)


class WomenCategory(ListView):
    model = Women
    template_name = 'women/index.html'
    context_object_name = 'posts'
    allow_empty = False  # Если коллекция posts пустая, генерируется ошибка 404

    def get_queryset(self):
        return Women.objects.filter(cat__slug=self.kwargs['cat_slug'])  # self.kwargs - словарь с параметрами маршрута, где cat_slug - имя параметра


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Категория - ' + str(context['posts'][0].cat)
        context['cat_selected'] = context['posts'][0].cat.slug
        return context




























def categories(request, catid):
    if request.GET:  # Также есть словарь request.POST, в котором данные, передающиеся на сервер: логин, пароль и т.д.
        print(
            request.GET)  # Выведется словарь в терминал, в котором будут параметры запроса в виде {'ключ': ['значение']}.
    if catid == 9:
        return HttpResponseRedirect(reverse('categories', args=[10]))
    return HttpResponse(f'<h1>Статьи по категориям</h1><p>{catid}</p>')


def archive(request, year):
    if int(year) > 2022:
        raise Http404()  # Автоматически будет перенаправление на функцию page_not_found.
    if int(year) == 1994:
        return redirect(
            'home')  # Указываем путь, куда перенаправляем. 302 redirect. Лучше указывать не путь, а имя маршрута.
    if int(year) == 1993:
        return redirect('home', permanent=True)  # 301 redirect.

    return HttpResponse(f'<h1>Запрос архива</h1><p>Год: {year}</p>')


def page_not_found(request, exception):
    return HttpResponseNotFound('Ошибка. Страница не найдена')


def test1(request):
    return render(request, 'women/test1.html', context = {'users': 1000})


def test2(request):
    return render(request, 'women/test2.html', context = {})
