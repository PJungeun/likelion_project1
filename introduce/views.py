from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone
from .models import Introduce_Post
from .forms import PostForm

# Create your views here.
def home(request):
    posts=Introduce_Post.objects
    return render(request,'introduce/home.html',{'posts':posts})

def detail(request,post_id):
    post_detail=get_object_or_404(Post,pk=post_id)
    return render(request,'introduce/detail.html',{'post':post_detail})

def post_new(request):
    if reques.method=="POST":
        form=PostForm(request.POST)
        if form.is_vaild():
            post=form.save(commit=False)
            post.published_date=timezone.datetime.now()
            post.save()
            return redirect('detail',post_id=post.pk)
    else:
        form=PostForm()
        return render(request,'introduce/new.html',{'form':form})
        