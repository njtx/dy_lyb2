from django.db import models

class msg(models.Model):
    name = models.CharField(max_length=100, verbose_name=u'姓名')
    email = models.CharField(max_length=100, verbose_name=u'邮箱')
    address = models.CharField(max_length=100, verbose_name=u'联系地址')
    messages = models.TextField(verbose_name=u'留言信息')

    class Meta:
        verbose_name = u'用户留言信息'