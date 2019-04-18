from django.http import HttpResponseRedirect
from django.shortcuts import render

from .models import Questions, Choices


# Create your views here.
# 定义视图函数


def lists(request):
    return render(request, template_name='votess/lists.html', context={'listss': Questions.objects.all()})


def ends(request, id):
    endss = Questions.objects.get(pk=id)
    return render(request, template_name='votess/ends.html', context={'endss': endss})


def counts(request, id):

    # print('aadsgad')
    # return HttpResponse('hello')
    endss = Questions.objects.get(pk=id)
    print(endss)

    count = request.POST['choo']
    print(count)
    # print('aadsgad')
    # return HttpResponse('hello')
    chooo = Choices.objects.get(pk=count)
    print(chooo)
    chooo.ccount += 1
    chooo.save()
    # return render(request, template_name='votess/counts.html', context={'endss': endss})
    return HttpResponseRedirect('/votes/counts/endss.id/', context={'endss': endss})
