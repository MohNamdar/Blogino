from django.shortcuts import render


# Create your views here.


def home(request):
    return render(request, 'blog/home.html')


def gallery(request):
    return render(request, 'blog/gallery.html')


def page(request):
    return render(request, 'blog/page.html')


def podcast_single(request):
    return render(request, 'blog/podcast_single.html')


def podcast_list(request):
    return render(request, 'blog/podcast_list.html')


def contact(request):
    return render(request, 'blog/contact.html')


def about(request):
    return render(request, 'blog/about.html')


def article_single(request):
    return render(request, 'blog/article_single.html')


def article_list(request):
    return render(request, 'blog/article_list.html')


def faq(request):
    return render(request, 'blog/faq.html')