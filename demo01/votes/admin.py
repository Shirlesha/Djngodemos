from django.contrib import admin

from .models import Choices, Questions


# Register your models here.


class ChoicesInline(admin.StackedInline):
    model = Choices
    extra = 1


class QuestionsAdmin(admin.ModelAdmin):
    # 显示字段，可以单击列头进行排序
    list_display = ['id', 'qcontain']
    # 过滤字段，过滤框会出现在右侧
    list_filter = ['qcontain']
    # 搜索字段，搜索框会出现在上侧，支持模糊查询
    search_fields = ['qcontain', 'id']
    # 分页，分页框会出现在下侧
    list_per_page = 10
    # 关联注册
    inlines = [ChoicesInline]


class ChoicesAdmin(admin.ModelAdmin):
    # 显示字段
    list_display = ['id', 'cchoose', 'ccount', 'cvalues']
    # 过滤字段
    list_filter = ['cchoose']
    # 搜索字段
    search_fields = ['cchoose']
    # 分页
    list_per_page = 10


admin.site.register(Choices, ChoicesAdmin)
admin.site.register(Questions, QuestionsAdmin)

