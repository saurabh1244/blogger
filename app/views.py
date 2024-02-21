from django.shortcuts import render
from .models import post ,comments
# Create your views here.


def home(request):
    obj = post.objects.all().order_by('-id')

    for x in obj:
        print(x.title)
    return render(request ,'index.html',{'obj':obj})


# def detail_page(request,idx):
#     cum_obj = None
#     if request.method == 'POST':
#         commentx = request.POST.get('cmt')
#         print(commentx)

#         obj = post.objects.get(id=idx)

#         cum_obj = comments.objects.create(cum_id=obj , text=commentx)
#         cum_obj.save()

#     obj = post.objects.get(id=idx)

#     comments = comments.objects.filter(cum_id=obj).order_by('-id')

#     return render(request,'detail.html',{'obj':obj,'comments':comments})


# def detail_page(request,idx):
#     obj = post.objects.get(id=idx)

#     if request.method == 'POST':
#         comment_text = request.POST.get('cmt')
#         print(comment_text)

#         new_comment = comments.objects.create(cum_id=obj , text=comment_text)
#         new_comment.save()

    
#     comments_list = comments.objects.filter(cum_id=obj).order_by('-id')

#     return render(request,'detail.html',{'obj':obj,'comments_list':comments_list})


def detail_page(request,slug):
    obj = post.objects.get(slugx=slug)

    if request.method == 'POST':
        comment_text = request.POST.get('cmt')
        print(comment_text)

        new_comment = comments.objects.create(cum_id=obj , text=comment_text)
        new_comment.save()

    
    comments_list = comments.objects.filter(cum_id=obj).order_by('-id')

    return render(request,'detail.html',{'obj':obj,'comments_list':comments_list})




def hero(request):
    return(render(request,'hero.html'))