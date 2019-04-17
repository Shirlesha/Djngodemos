from django.contrib import admin
from .models import BookInfo, HeroInfo
# Register your models here.


class HeroInfoInline(admin.StackedInline):
    model = HeroInfo
    # 关联个数
    extra = 1


class BookInfoAdmin(admin.ModelAdmin):
    # 显示字段，可以单击列头进行排序
    list_display = ['id', 'bname', 'bpub_date']
    # 过滤字段，过滤框会出现在右侧
    list_filter = ['bname']
    # 搜索字段，搜索框会出现在上侧，支持模糊查询
    search_fields = ['bname']
    # 分页，分页框会出现在下侧
    list_per_page = 2
    # 关联注册
    inlines = [HeroInfoInline]


class HeroInfoAdmin(admin.ModelAdmin):
    # 显示字段
    list_display = ['id', 'name', 'hgender', 'skills', 'hbook']
    # 过滤字段
    list_filter = ['hname']
    # 搜索字段
    search_fields = ['hname']
    # 分页
    list_per_page = 2





admin.site.register(BookInfo, BookInfoAdmin)
admin.site.register(HeroInfo, HeroInfoAdmin)

'''
通过少量的代码实现强大的后台管理
需要将特定的数据模型注册后才能在后台管理
'''