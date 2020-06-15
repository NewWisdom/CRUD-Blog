from django.shortcuts import render, redirect,get_object_or_404
from .models import Post
from .forms import PostForm

# Create your views here.

def main(request):
    posts=Post.objects # Post.object를 posts 변수에 담기
    return render(request, 'posts.html',{'posts':posts})

def create(request):
    if request.method=='POST':
        form=PostForm(request.POST) # form 변숭에 PostForm 할당
        if form.is_valid(): #form 유효성 검증
            form.save()
            return redirect('main') # main페이지로 가기
    else:
        form =PostForm() # 빈 form 열기
    return render(request,'create.html',{'form':form})

def detail(request,pk):
    post=get_object_or_404(Post, pk=pk)#해당 객체가 있으면 가져오고 없으면 404 에러, pk 로 pk 사용
    return render(request,'detail.html',{'post':post})

def update(request,pk):
    post=get_object_or_404(Post,pk=pk)
    if request.method=='POST':
        form = PostForm(request.POST,instance=post)
        if form.is_valid():
            form.save()
            return redirect('main')
    else:
        form=PostForm(instance=post)
    return render(request,'update.html',{'form':form})

def delete(request,pk):
    post=Post.objects.get(pk=pk)
    post.delete()#delete함수 실행
    return redirect('main')