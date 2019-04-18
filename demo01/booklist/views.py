from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from .models import BookInfo, HeroInfo


# Create your views here.

# 定义视图函数


def index(request):
    # print("请求", request)
    # return HttpResponse("首页")
    # print('首页')
    # # 加载模板
    # indextem = loader.get_template('books/index.html')
    # cont = {'username': 'Shirlesha'}
    # # 使用变量参数渲染模板
    # result = indextem.render(cont)
    # # 返回模板
    # return HttpResponse(result)
    return render(request, template_name='books/index.html', context={'username': 'Shirlesha'})


def list(request):
    # # return HttpResponse("列表页")
    # listtem = loader.get_template('books/list.html')
    # cont = {}
    # result = listtem.render(cont)
    # return HttpResponse(result)
    return render(request, template_name='books/list.html', context={'books': BookInfo.objects.all()})


def detail(request, id):
    # # try:
    # #     b = BookInfo.objects.get(pk=id)
    # #     return HttpResponse(b)
    # # except:
    # #     return HttpResponse("书名不存在")
    # detailtem = loader.get_template('books/detail.html')
    # cont = {}
    # result = detailtem.render(cont)
    # return HttpResponse(result)
    books = BookInfo.objects.get(pk=id)
    return render(request, template_name='books/detail.html', context={'books': books})


def infoss(request, id):
    roles = HeroInfo.objects.get(pk=id)
    return render(request, template_name='books/infoss.html', context={'roles': roles})


def add(request):
    # BookInfo.add_to_class(bookname)
    # return HttpResponse("添加成功")
    books = request.POST['bookname']
    return HttpResponse("添加成功")

    print(books)
    # book = BookInfo()
    #     # book.bname = books
    #     # book.bpub_date = datetime.datetime
    #     # print(book.bpub_date)
    return render(request, template_name='books/add.html', context={'books': BookInfo.objects.all()})


def delete(request, id):
    # print(BookInfo.objects.get(pk=id))
    # BookInfo.objects.get(pk=id).delete()
    # return HttpResponseRedirect('books/list.html', {'books': BookInfo.objects.all()})
    # # return render(request, template_name='books/list.html', context={'books': BookInfo.objects.all()})
    try:
        BookInfo.objects.get(pk=id).delete()
        bl = BookInfo.objects.all()
        # 使用render没有刷新请求url
        # return render(request, 'booktest/list.html', {"booklist": bl})
        # 重新向服务器发起请求 刷新url
        # 这里不知道为什么不可以去除硬编码
        return HttpResponseRedirect('/booklist/booklist/', {"booklist": bl})
    except:
        return HttpResponse("删除失败")

'''
视图函数
将函数和路由绑定
'''