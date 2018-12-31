from django.shortcuts import render, redirect
from .models import Friends,Comment
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.
def friends(request):
    friends = Friends.objects.all().order_by('name')
    return render(request, 'friends/friends.html', {'friends': friends})

def friends_details(request, slug):
    #return HttpResponse(slug)
    details = Friends.objects.get(slug=slug)
    comments = Comment.objects.filter(friend=details).order_by('created')
    return render(request, 'friends/friends_details.html', {'details': details,'comments':comments})


@login_required(login_url='/accounts/login/')
def friends_create(request):
    if request.method == "POST":
        form = forms.CreateFriends(request.POST, request.FILES)
        if form.is_valid():
            # save friend to db
            instance = form.save(commit=False)
            instance.username = request.user
            instance.save()
            return redirect('friends:list')
    else:
        form = forms.CreateFriends()
    return render(request, 'friends/friends_create.html', {'form':form})

@login_required(login_url="/accounts/login")
def add_comment(request, slug):
    friend = Friends.objects.get(slug=slug)
    if request.method == "POST":
        form = forms.CreateComment(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.username = request.user
            instance.friend = friend
            instance.save()
            return redirect('friends:details', slug=slug)
    else:
        form = forms.CreateComment()
    return render(request, 'friends/comment_create.html', {'form': form, 'friend':friend})
