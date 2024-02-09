from django.shortcuts import render , HttpResponse
from .models import blogx ,comment

def page(request):
    obj = blogx.objects.all()
    context = {
        'datas': obj
    }
    return render(request , 'index.html',context)
    

def home(request):
       return render(request, 'home.html')



def post(request,slug):
    cum_obj = None
    if request.method == 'POST':
        commentx = request.POST['comment']
        print(comment)

        obj = blogx.objects.get(slugx=slug)

        cum_obj = comment.objects.create(cum_id=obj,text=commentx)
        cum_obj.save()
        print("succefully added comments...")

    obj = blogx.objects.get(slugx=slug)
    comments = comment.objects.filter(cum_id=obj).order_by('-id')

    context = {
        'html':obj,
        'new_comment':cum_obj,
        'comments':comments
    }

    return render(request , 'datax.html',context)