import hashlib

from django.core.mail import EmailMultiAlternatives
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from pyecharts import Bar, Pie, Line

from demo import models
import datetime


def register_form(request):

    return render(request, 'register.html')


def hash_code(name, now):
    """
    使用加密的方式对传输带参数进行加密
    :param name:用户名
    :param now:当前时间
    :return:加密后的字符串
    """
    h = hashlib.md5()
    code = name + now
    h.update(code.encode())
    return h.hexdigest()

def make_string(new_user):
    """
    用来给每一个用户生成一个唯一不可重的注册码
    :param new_user:当前用户
    :return:生成完成的验证码
    """
    now = datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")
    code = hash_code(new_user.name, now)
    models.ConfirmString.objects.create(code=code, user=new_user)

    return code


def send_email(email, code):
    """
    用来真正发送邮件发方法
    :param email:用户的邮箱号
    :param code:唯一的注册码
    :return:
    """
    subject, from_email, to = '来自153的测试邮件', '18500230996@sina.cn', 'maoxinyu925@163.com'
    text_content = '欢迎访问www.baidu.com，祝贺你收到了我的邮件，有幸收到我的邮件说明你及其幸运'
    html_content = '<p>感谢注册<a href="http://{}/confirm/?code={}"target = blank > www.baidu.com < / a >，\欢迎你来验证你的邮箱，验证结束你就可以登录了！ < / p > '.format('127.0.0.1:8000', code)
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()


def register_real(request):
    """
    用来真正处理注册表单的视图
    :param request:表单参数
    :return:
    """
    username = request.POST.get("username")
    password = request.POST.get('password')
    email = request.POST.get("email")
    new_user = models.User.objects.create(name=username, password=password, email=email)
    code = make_string(new_user)
    send_email(email, code)
    return render(request, 'login.html')


def confirm(request):
    """
    用来处理用户点击邮箱中的连接来验证邮箱是否可用的视图
    :param request:
    :return:
    """
    code = request.GET.get('code')
    print(code)
    # 判断请求的注册码是否与数据库中该用户保存的一致

    # 将该用户的状态改为可用

    # 删除注册码

    # 跳转到登陆的页面

    return HttpResponse()


def forst_charts(request):

    attr = ['UV', 'PV', '羊毛', '杨修', '张无忌']
    value = ['20', '30', '40', '15', '45']
    pie = Line('饼图')
    pie.add("名字", attr, value, is_label_show=True, is_more_utils=True)
    pie.render('./main.html')
    return HttpResponse()
