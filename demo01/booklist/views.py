from django.shortcuts import render
from django.http import HttpResponse
from .models import BookInfo, HeroInfo
from django.template import loader
from django.shortcuts import render
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

'''
视图函数
将函数和路由绑定
'''