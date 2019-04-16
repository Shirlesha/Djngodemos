from django.db import models


class BookInfo(models.Model):
    bname = models.CharField(max_length=20)
    bpub_date = models.DateTimeField(auto_now_add=True)


class HeroInfo(models.Model):
    hname = models.CharField(max_length=20)
    hgender = models.BooleanField()
    hcontent = models.CharField(max_length=100)
    # 外键 第一个参数为表名 第二个参数代表删除类型
    hbook = models.ForeignKey('BookInfo', on_delete=models.CASCADE)



# Create your models here.

'''
django MVT M
ORM 对象中O
定义模型：继承models.Model
配置数据库：默认的是SQLite
将应用名添加到应用列表installed_apps

python manage.py makemigrations 生成迁移文件
python manage.py migrate 执行迁移
'''
'''
python manage.py shell进入命令：不需要运行项目就可以操作数据库
导入类来自bootlist.models 导入HeroInfo,BookInfo
查找所有行表民.objects.all()
根据主键查找表名.objects.get(pk=1)
添加对象 对象.save()
修改对象 对象.save()
删除对象 对象.delete()
一对多：一方存在主键 ，多方存在主键也存在外键（一方中主键）
一方.heroinfo_set.all()
类名.object.create(列名=值)不需要保存
'''
