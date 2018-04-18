from django.shortcuts import render
from .models import msg

def getmsg(request):
    #查询
    # ulist = msg.objects.all()
    # print([i for i in ulist])
    #
    # print(request)
    # return render(request, 'message/message_form.html', context={
    #     'title': '欢迎留言...',
    #     'list': [i for i in ulist][0]
    # })

    #新增

    TITLE = '欢迎留言...'
    if request.method == 'POST':
        # 获取value值，取不到为空

        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address', '')
        message = request.POST.get('message', '')

        user_message = msg()
        user_message.name = name
        user_message.email = email
        user_message.address = address
        user_message.messages = message
        user_message.save()

    return render(request, 'message/message_form.html', context={
        'title': TITLE
    })



