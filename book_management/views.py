from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from book_management.models import Category,Book

def index(request):
    cat_num = len(Category.objects.all())
    book_num = len(Book.objects.all())
    books = Book.objects.all()
    #template = loader.get_template('index.html')
    context = {
        'category_num': cat_num,
        'book_num': book_num,
        'books' : books,
    }
    return render(request,'index.html',context)
# Create your views here.

def image_saver(request):
    import urllib.request
    url = request.GET["url"]
    ##url = 'https://www.marlborough.govt.nz/repository/libraries/id:1w1mps0ir17q9sgxanf9/hierarchy/Standard%20Images%20Reusable/Watercourse_river_stream_GCI.jpg'
    urllib.request.urlretrieve(url, "./media/book_image/river.jpg")

    Book.objects.filter(id=3).update(bookImage='book_image/river.jpg')

    return HttpResponse("Download Success")